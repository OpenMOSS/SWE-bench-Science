# Publication attribution and change notice

This document is derived from Juan Luis Cano Rodríguez and Jorge Martínez
Garrido, "poliastro: a Python library for interactive astrodynamics,"
*Proceedings of the 21st Python in Science Conference* (2022),
<https://doi.org/10.25080/majora-212e5952-015>.

- Copyright: 2022, the paper authors.
- License: Creative Commons Attribution 3.0 Unported,
  <https://creativecommons.org/licenses/by/3.0/>.
- Source:
  <https://github.com/scipy-conference/scipy_proceedings/tree/2022/papers/juanluis_cano_poliastro>.
- Changes: the upstream reStructuredText was converted to Markdown and its
  reusable figures were localized for offline use. One third-party textbook
  figure was omitted because no redistribution permission was identified.
  Citation keys are resolved by `paper_assets/refs.bib`.

author  
Juan Luis Cano Rodríguez

email  
<hello@juanlu.space>

orcid  
0000-0002-2187-161X

institution  
Unaffiliated

corresponding  

author  
Jorge Martínez Garrido

email  
<contact@jorgemartinez.space>

institution  
Unaffiliated

bibliography  
paper_assets/refs.bib

video  
<https://www.youtube.com/watch?v=VCpTgU1pb5k>

# poliastro: a Python library for interactive astrodynamics

<div class="abstract">

Space is more popular than ever, with the growing public awareness of interplanetary scientific missions, as well as the increasingly large number of satellite companies planning to deploy satellite constellations. Python has become a fundamental technology in the astronomical sciences, and it has also caught the attention of the Space Engineering community.

One of the requirements for designing a space mission is studying the trajectories of satellites, probes, and other artificial objects, usually ignoring non-gravitational forces or treating them as perturbations: the so-called n-body problem. However, for preliminary design studies and most practical purposes, it is sufficient to consider only two bodies: the object under study and its attractor.

Even though the two-body problem has many analytical solutions, orbit propagation (the initial value problem) and targeting (the boundary value problem) remain computationally intensive because of long propagation times, tight tolerances, and vast solution spaces. On the other hand, astrodynamics researchers often do not share the source code they used to run analyses and simulations, which makes it challenging to try out new solutions.

This paper presents poliastro, an open-source Python library for interactive astrodynamics that features an easy-to-use API and tools for quick visualization. poliastro implements core astrodynamics algorithms (such as the resolution of the Kepler and Lambert problems) and leverages numba, a Just-in-Time compiler for scientific Python, to optimize the running time. Thanks to Astropy, poliastro can perform seamless coordinate frame conversions and use proper physical units and timescales. At the moment, poliastro is the longest-lived Python library for astrodynamics, has contributors from all around the world, and several New Space companies and people in academia use it.

</div>

<div class="keywords">

astrodynamics, orbital mechanics, orbit propagation, orbit visualization, two-body problem

</div>

## Introduction

### History

The term "astrodynamics" was coined by the American astronomer Samuel Herrick, who received encouragement from the space pioneer Robert H. Goddard, and refers to the branch of space science dealing with the motion of artificial celestial bodies (duboshin_book_1973, herrick_astrodynamics_1971). However, the roots of its mathematical foundations go back several centuries.

Kepler first introduced his laws of planetary motion in 1609 and 1619 and derived his famous transcendental equation (`eq:kepler`), which we now see as capturing a restricted form of the two-body problem. This work was generalized by Newton to give birth to the n-body problem, and many other mathematicians worked on it throughout the centuries (Daniel and Johann Bernoulli, Euler, Gauss). Poincaré established in the 1890s that no general closed-form solution exists for the n-body problem, since the resulting dynamical system is chaotic battin_introduction_1999. Sundman proved in the 1900s the existence of convergent solutions for a few restricted with $`n = 3`$.

<span label="eq:kepler">
``` math
M = E - e \sin{E}
```
</span>

In 1903 Tsiokovsky evaluated the conditions required for artificial objects to leave the orbit of the earth; this is considered as a foundational contribution to the field of astrodynamics. Tsiokovsky devised equation `eq:tsiolkovsky` which relates the increase in velocity with the effective exhaust velocity of thrusted gases and the fraction of used propellant.

<span label="eq:tsiolkovsky">
``` math
\Delta v = v_e \ln \frac{m_0}{m_f}
```
</span>

Further developments by Kondratyuk, Hohmann, and Oberth in the early 20th century all added to the growing field of orbital mechanics, which in turn enabled the development of space flight in the USSR and the United States in the 1950s and 1960s.

### The two-body problem

In a system of $`i \in {1, ..., n}`$ bodies subject to their mutual attraction, by application of Newton's law of universal gravitation, the total force $`\vec{f}_i`$ affecting $`m_i`$ due to the presence of the other $`n - 1`$ masses is given by battin_introduction_1999:

<span label="eq:gravforces">
``` math
\vec{f}_i = -G \sum_{j \neq i}^n \frac{m_i m_j}{|\vec{r}_{ij}|^3} \vec{r}_{ij}
```
</span>

where $`G = 6.67430\cdot 10^{-11}~\text{N m$^2$ kg$^{-2}$}`$ is the universal gravitational constant, and $`\vec{r}_{ij}`$ denotes the position vector from $`m_i`$ to $`m_j`$. Applying Newton's second law of motion results in a system of $`n`$ differential equations:

<span label="eq:nbody">
``` math
\frac{\diff^2{\vec{r}}_i}{\diff{t}^2} = -G \sum_{j \neq i}^n \frac{m_j}{|\vec{r}_{ij}|^3} \vec{r}_{ij}
```
</span>

By setting $`n = 2`$ in `eq:nbody` and subtracting the two resulting equalities, one arrives to the **fundamental equation of the two-body problem**:

<span label="eq:twobody">
``` math
\frac{\diff^2{\vec{r}}}{\diff{t}^2} = -\frac{\mu}{r^3} \vec{r}
```
</span>

where $`\mu = G(m_1 + m_2) = G(M + m)`$. When $`m \ll M`$ (for example, an artificial satellite orbiting a planet), one can consider $`\mu = GM`$ a property of the attractor.

### Keplerian vs non-keplerian motion

Conveniently manipulating equation `eq:twobody` leads to several properties battin_introduction_1999 that were already published by Johannes Kepler in the 1610s, namely:

1.  The orbit always describes a conic section (an ellipse, a parabola, or an hyperbola), with the attractor at one of the two foci and can be written in polar coordinates like $`r = \frac{p}{1 + e \cos{\nu}}`$ (Kepler's first law).
2.  The magnitude of the specific angular momentum $`h = r^2 \frac{\diff{\theta}}{\diff t}`$ is constant an equal to two times the areal velocity (Kepler's second law).
3.  For closed (circular and elliptical) orbits, the period is related to the size of the orbit through $`P = 2 \pi \sqrt{\frac{a^3}{\mu}}`$ (Kepler's third law).

For many practical purposes it is usually sufficient to limit the study to one object orbiting an attractor and ignore all other external forces of the system, hence restricting the study to trajectories governed by equation `eq:twobody`. Such trajectories are called "Keplerian", and several problems can be formulated for them:

- The **initial-value problem**, which is usually called **propagation**, involves determining the position and velocity of an object after an elapse period of time given some initial conditions.
- **Preliminary orbit determination**, which involves using exact or approximate methods to derive a Keplerian orbit from a set of observations.
- The **boundary-value problem**, often named **the Lambert problem**, which involves determining a Keplerian orbit from boundary conditions, usually departure and arrival position vectors and a time of flight.

Fortunately, most of these problems boil down to finding numerical solutions to relatively simple algebraic relations between time and angular variables: for elliptic motion ($`0 \le e < 1`$) it is the Kepler equation, and equivalent relations exist for the other eccentricity regimes battin_introduction_1999. Numerical solutions for these equations can be found in a number of different ways, each one with different complexity and precision tradeoffs. In the Methods section we list the ones implemented by poliastro.

On the other hand, there are many situations in which natural and artificial orbital perturbations must be taken into account so that the actual non-Keplerian motion can be properly analyzed:

- Interplanetary travel in the proximity of other planets. On a first approximation it is usually enough to study the trajectory in segments and focus the analysis on the closest attractor, hence patching several Keplerian orbits along the way (the so-called "patched-conic approximation") battin_introduction_1999. The boundary surface that separates one segment from the other is called the sphere of influence.
- Use of solar sails, electric propulsion, or other means of continuous thrust. Devising the optimal guidance laws that minimize travel time or fuel consumption under these conditions is usually treated as an optimization problem of a dynamical system, and as such it is particularly challenging conway_spacecraft_2014.
- Artificial satellites in the vicinity of a planet. This is the regime in which all the commercial space industry operates, especially for those satellites in Low-Earth Orbit (LEO).

### State of the art

In our view, at the time of creating poliastro there were a number of issues with existing open source astrodynamics software that posed a barrier of entry for novices and amateur practitioners. Most of these barriers still exist today and are described in the following paragraphs. The goals of the project can be condensed as follows:

1.  Set an example on reproducibility and good coding practices in astrodynamics.
2.  Become an approachable software even for novices.
3.  Offer a performant software that can be also used in scripting and interactive workflows.

The most mature software libraries for astrodynamics are arguably Orekit noauthor_orekit_2022, a "low level space dynamics library written in Java" with an open governance model, and SPICE noauthor_spice_2022, a toolkit developed by NASA's Navigation and Ancillary Information Facility at the Jet Propulsion Laboratory. Other similar, smaller projects that appeared later on and that are still maintained to this day include PyKEP izzo_esapykep_2020, beyond noauthor_beyond_2022, tudatpy noauthor_tudatpy_2022, sbpy mommert_sbpy_2019, Skyfield rhodes_skyfield_2020 (Python), CelestLab (Scilab) noauthor_celestlab_2022, astrodynamics.jl (Julia) noauthor_astrodynamicsjl_nodate and Nyx (Rust) noauthor_nyx_2021. In addition, there are some Graphical User Interface (GUI) based open source programs used for Mission Analysis and orbit visualization, such as GMAT noauthor_gmat_2020 and gpredict noauthor_gpredict_2018, and complete web applications for tracking constellations of satellites like the SatNOGS project by the Libre Space Foundation noauthor_satnogs_2021.

The level of quality and maintenance of these packages is somewhat heterogeneous. Community-led projects with a strong corporate backing like Orekit are in excellent health, while on the other hand smaller projects developed by volunteers (beyond, astrodynamics.jl) or with limited institutional support (PyKEP, GMAT) suffer from lack of maintenance. Part of the problem might stem from the fact that most scientists are never taught how to build software efficiently, let alone the skills to collaboratively develop software in the open wilson_best_2014, and astrodynamicists are no exception.

On the other hand, it is often difficult to translate the advances in astrodynamics research to software. Classical algorithms developed throughout the 20th century are described in papers that are sometimes difficult to find, and source code or validation data is almost never available. When it comes to modern research carried in the digital era, source code and validation data is still difficult, even though they are supposedly provided "upon reasonable request" stodden_empirical_2018 gabelica_many_2022.

It is no surprise that astrodynamics software often requires deep expertise. However, there are often implicit assumptions that are not documented with an adequate level of detail which originate widespread misconceptions and lead even seasoned professionals to make conceptual mistakes. Some of the most notorious misconceptions arise around the use of general perturbations data (OMMs and TLEs) finkleman_tle_2007, the geometric interpretation of the mean anomaly battin_introduction_1999, or coordinate transformations vallado_revisiting_2006.

Finally, few of the open source software libraries mentioned above are amenable to scripting or interactive use, as promoted by computational notebooks like Jupyter kluyver_jupyter_2016.

The following sections will now discuss the various areas of current research that an astrodynamicist will engage in, and how poliastro improves their workflow.

## Methods

### Software Architecture

The architecture of poliastro emerges from the following set of conflicting requirements:

1.  There should be a high-level API that enables users to perform orbital calculations in a straightforward way and prevent typical mistakes.
2.  The running time of the algorithms should be within the same order of magnitude of existing compiled implementations.
3.  The library should be written in a popular open-source language to maximize adoption and lower the barrier to external contributors.

One of the most typical mistakes we set ourselves to prevent with the high-level API is dimensional errors. Addition and substraction operations of physical quantities are defined only for quantities with the same units drobot_foundations_1953: for example, the operation $`1~\text{km} + 100~\text{m}`$ requires a scale transformation of at least one of the operands, since they have different units (kilometers and meters) but the same dimension (length), whereas the operation $`1~\text{km} + 1~\text{kg}`$ is directly not allowed because dimensions are incompatible (length and mass). As such, software systems operating with physical quantities should raise exceptions when adding different dimensions, and transparently perform the required scale transformations when adding different units of the same dimension.

With this in mind, we evaluated several Python packages for unit handling (see j_goldbaum_unyt_2018 for a recent survey) and chose `astropy.units` the_astropy_collaboration_astropy_2018.

``` python
radius = 6000  # km
altitude = 500  # m

# Wrong!
distance = radius + altitude  

from astropy import units as u

# Correct
distance = (radius << u.km) + (altitude << u.m)
```

This notion of providing a "safe" API extends to other parts of the library by leveraging other capabilities of the Astropy project. For example, timestamps use `astropy.time` objects, which take care of the appropriate handling of time scales (such as TDB or UTC), reference frame conversions leverage `astropy.coordinates`, and so forth.

One of the drawbacks of existing unit packages is that they impose a significant performance penalty. Even though `astropy.units` is integrated with NumPy, hence allowing the creation of array quantities, all the unit compatibility checks are implemented in Python and require lots of introspection, and this can slow down mathematical operations by several orders of magnitude. As such, to fulfill our desired performance requirement for poliastro, we envisioned a two-layer architecture:

- The **Core API** follows a procedural style, and all the functions receive Python numerical types and NumPy arrays for maximum performance.
- The **High level API** is object-oriented, all the methods receive Astropy `Quantity` objects with physical units, and computations are deferred to the Core API.

Most of the methods of the High level API consist only of the necessary unit compatibility checks, plus a wrapper over the corresponding Core API function that performs the actual computation.

``` python
@u.quantity_input(E=u.rad, ecc=u.one)
def E_to_nu(E, ecc):
    """True anomaly from eccentric anomaly."""
    return (
        E_to_nu_fast(
            E.to_value(u.rad),
            ecc.value
        ) << u.rad
    ).to(E.unit)
```

As a result, poliastro offers a unit-safe API that performs the least amount of computation possible to minimize the performance penalty of unit checks, and also a unit-unsafe API that offers maximum performance at the cost of not performing any unit validation checks.

<figure class="align-center">
<embed src="paper_assets/architecture.pdf" />
<figcaption>poliastro two-layer architecture <code class="interpreted-text" role="label">architecture</code></figcaption>
</figure>

Finally, there are several options to write performant code that can be used from Python, and one of them is using a fast, compiled language for the CPU intensive parts. Successful examples of this include NumPy, written in C harris_array_2020, SciPy, featuring a mix of FORTRAN, C, and C++ code virtanen_scipy_2020, and pandas, making heavy use of Cython behnel_cython_2011. However, having to write code in two different languages hinders the development speed, makes debugging more difficult, and narrows the potential contributor base (what Julia creators called "The Two Language Problem" bezanson_julia_2017).

As authors of poliastro we wanted to use Python as the sole programming language of the implementation, and the best solution we found to improve its performance was to use Numba, a LLVM-based Python JIT compiler lam_numba_2015.

## Usage

### Basic `Orbit` and `Ephem` creation

The two central objects of the poliastro high level API are `Orbit` and `Ephem`:

- `Orbit` objects represent an osculating (hence Keplerian) orbit of a dimensionless object around an attractor at a given point in time and a certain reference frame.
- `Ephem` objects represent an ephemerides, a sequence of spatial coordinates over a period of time in a certain reference frame.

There are six parameters that uniquely determine a Keplerian orbit, plus the gravitational parameter of the corresponding attractor ($`k`$ or $`\mu`$). Optionally, an epoch that contextualizes the orbit can be included as well. This set of six parameters is not unique, and several of them have been developed over the years to serve different purposes. The most widely used ones are:

- **Cartesian elements**: Three components for the position $`(x, y, z)`$ and three components for the velocity $`(v_x, v_y, v_z)`$. This set has no singularities.
- **Classical Keplerian elements**: Two components for the shape of the conic (usually the semimajor axis $`a`$ or semiparameter $`p`$ and the eccentricity $`e`$), three Euler angles for the orientation of the orbital plane in space (inclination $`i`$, right ascension of the ascending node $`\Omega`$, and argument of periapsis $`\omega`$), and one polar angle for the position of the body along the conic (usually true anomaly $`f`$ or $`\nu`$). This set of elements has an easy geometrical interpretation and the advantage that, in pure two-body motion, five of them are fixed $`(a, e, i, \Omega, \omega)`$ and only one is time-dependent ($`\nu`$), which greatly simplifies the analytical treatment of orbital perturbations. However, they suffer from singularities steming from the Euler angles ("gimbal lock") and equations expressed in them are ill-conditioned near such singularities.
- **Walker modified equinoctial elements**: Six parameters $`(p, f, g, h, k, L)`$. Only $`L`$ is time-dependent and this set has no singularities, however the geometrical interpretation of the rest of the elements is lost walker_set_1985.

Here is how to create an `Orbit` from cartesian and from classical Keplerian elements. Walker modified equinoctial elements are supported as well.

``` python
from astropy import units as u

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit
from poliastro.constants import J2000

# Data from Curtis, example 4.3
r = [-6045, -3490, 2500] << u.km
v = [-3.457, 6.618, 2.533] << u.km / u.s

orb_curtis = Orbit.from_vectors(
   Earth,  # Attractor
   r, v  # Elements
)

# Data for Mars at J2000 from JPL HORIZONS
a = 1.523679 << u.au
ecc = 0.093315 << u.one
inc = 1.85 << u.deg
raan = 49.562 << u.deg
argp = 286.537 << u.deg
nu = 23.33 << u.deg

orb_mars = Orbit.from_classical(
   Sun,
   a, ecc, inc, raan, argp, nu,
   J2000  # Epoch
)
```

When displayed on an interactive REPL, `Orbit` objects provide basic information about the geometry, the attractor, and the epoch:

``` pycon
>>> orb_curtis
7283 x 10293 km x 153.2 deg (GCRS) orbit
around Earth (X) at epoch J2000.000 (TT)

>>> orb_mars
1 x 2 AU x 1.9 deg (HCRS) orbit
around Sun (X) at epoch J2000.000 (TT)
```

Similarly, `Ephem` objects can be created using a variety of classmethods as well. Thanks to `astropy.coordinates` built-in low-fidelity ephemerides, as well as its capability to remotely access the JPL HORIZONS system, the user can seamlessly build an object that contains the time history of the position of any Solar System body:

``` python
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris

from poliastro.ephem import Ephem

# Configure high fidelity ephemerides globally
# (requires network access)
solar_system_ephemeris.set("jpl")

# For predefined poliastro attractors
earth = Ephem.from_body(Earth, Time.now().tdb)

# For the rest of the Solar System bodies
ceres = Ephem.from_horizons("Ceres", Time.now().tdb)
```

There are some crucial differences between `Orbit` and `Ephem` objects:

- `Orbit` objects have an attractor, whereas `Ephem` objects do not. Ephemerides can originate from complex trajectories that don't necessarily conform to the ideal two-body problem.
- `Orbit` objects capture a precise instant in a two-body motion plus the necessary information to propagate it forward in time indefinitely, whereas `Ephem` objects represent a bounded time history of a trajectory. This is because the equations for the two-body motion are known, whereas an ephemeris is either an observation or a prediction that cannot be extrapolated in any case without external knowledge. As such, `Orbit` objects have a `.propagate` method, but `Ephem` ones do not. This prevents users from attempting to propagate the position of the planets, which will always yield poor results compared to the excellent ephemerides calculated by external entities.

Finally, both types have methods to convert between them:

- `Ephem.from_orbit` is the equivalent of sampling a two-body motion over a given time interval. As explained above, the resulting `Ephem` loses the information about the original attractor.
- `Orbit.from_ephem` is the equivalent of calculating the osculating orbit at a certain point of a trajectory, assuming a given attractor. The resulting `Orbit` loses the information about the original, potentially complex trajectory.

### Orbit propagation

`Orbit` objects have a `.propagate` method that takes an elapsed time and returns another `Orbit` with new orbital elements and an updated epoch:

``` pycon
>>> from poliastro.examples import iss

>>> iss
>>> 6772 x 6790 km x 51.6 deg (GCRS) ...

>>> iss.nu.to(u.deg)
<Quantity 46.59580468 deg>

>>> iss_30m = iss.propagate(30 << u.min)

>>> (iss_30m.epoch - iss.epoch).datetime
datetime.timedelta(seconds=1800)

>>> (iss_30m.nu - iss.nu).to(u.deg)
<Quantity 116.54513153 deg>
```

The default propagation algorithm is an analytical procedure described in farnocchia_robust_2013 that works seamlessly in the near parabolic region. In addition, poliastro implements analytical propagation algorithms as described in danby_solution_1983, odell_procedures_1986, markley_kepler_1995, mikkola_cubic_1987, pimienta-penalver_accurate_2013, charls_recursive_2022, and vallado_fundamentals_2007.

### Natural perturbations

<figure class="align-center">
<embed src="paper_assets/enckes_method.pdf" />
<figcaption>Osculating (Keplerian) vs perturbed (true) orbit. Original diagram
by GregorDS, "File:Enckes method-vector.svg," Wikimedia Commons,
<https://commons.wikimedia.org/wiki/File:Enckes_method-vector.svg>, licensed
under CC BY-SA 4.0,
<https://creativecommons.org/licenses/by-sa/4.0/>. The SciPy proceedings
version converted the diagram to PDF. <code class="interpreted-text"
role="label">fig:osculating</code></figcaption>
</figure>

As showcased in Figure `fig:osculating`, at any point in a trajectory we can define an ideal Keplerian orbit with the same position and velocity under the attraction of a point mass: this is called the osculating orbit. Some numerical propagation methods exist that model the true, perturbed orbit as a deviation from an evolving, osculating orbit. poliastro implements Cowell's method cowell_investigation_1910, which consists in adding all the perturbation accelerations and then integrating the resulting differential equation with any numerical method of choice:

<span label="eq:cowell">
``` math
\frac{\diff^2{\vec{r}}}{\diff{t}^2} = -\frac{\mu}{r^3} \vec{r} + \vec{a}_d
```
</span>

The resulting equation is usually integrated using high order numerical methods, since the integration times are quite large and the tolerances comparatively tight. An in-depth discussion of such methods can be found in hairer_solving_2009. poliastro uses Dormand-Prince 8(5,3) (`DOP853`), a commonly used method available in SciPy harris_array_2020.

There are several natural perturbations included: J2 and J3 gravitational terms, several atmospheric drag models (exponential, jacchia_thermospheric_1977, atmosphere_us_1962, atmosphere_us_1976), and helpers for third body gravitational attraction and radiation pressure as described in curtis_orbital_2008.

``` python
@njit
def combined_a_d(
    t0, state, k, j2, r_eq, c_d, a_over_m, h0, rho0
):
    return (
        J2_perturbation(
            t0, state, k, j2, r_eq
        ) + atmospheric_drag_exponential(
            t0, state, k, r_eq, c_d, a_over_m, h0, rho0
        )
    )

def f(t0, state, k):
    du_kep = func_twobody(t0, state, k)
    ax, ay, az = combined_a_d(
        t0,
        state,
        k,
        R=R,
        C_D=C_D,
        A_over_m=A_over_m,
        H0=H0,
        rho0=rho0,
        J2=Earth.J2.value,
    )
    du_ad = np.array([0, 0, 0, ax, ay, az])

    return du_kep + du_ad

rr = propagate(
    orbit,
    tofs,
    method=cowell,
    f=f,
)
```

### Continuous thrust control laws

Beyond natural perturbations, spacecraft can modify their trajectory on purpose by using impulsive maneuvers (as explained in the next section) as well as continuous thrust guidance laws. The user can define custom guidance laws by providing a perturbation acceleration in the same way natural perturbations are used. In addition, poliastro includes several analytical solutions for continuous thrust guidance laws with specific purposes, as studied in cano_rodriguez_study_2017: optimal transfer between circular coplanar orbits edelbaum_propulsion_1961 burt_space_1967, optimal transfer between circular inclined orbits edelbaum_propulsion_1961 kechichian_reformulation_1997, quasi-optimal eccentricity-only change pollard_simplified_1997, simultaneous eccentricity and inclination change pollard_simplified_2000, and agument of periapsis adjustment pollard_evaluation_1998. A much more rigorous analysis of a similar set of laws can be found in di_carlo_analytical_2021.

``` python
from poliastro.twobody.thrust import change_ecc_inc

ecc_f = 0.0 << u.one
inc_f = 20.0 << u.deg
f = 2.4e-6 << (u.km / u.s**2)

a_d, _, t_f = change_ecc_inc(orbit, ecc_f, inc_f, f)
```

### Impulsive maneuvers

Impulsive maneuvers are modeled considering a change in the velocity of a spacecraft while its position remains fixed. The `poliastro.maneuver.Maneuver` class provides various constructors to instantiate popular impulsive maneuvers in the framework of the non-perturbed two-body problem:

- `Maneuver.impulse`
- `Maneuver.hohmann`
- `Maneuver.bielliptic`
- `Maneuver.lambert`

``` python
from poliastro.maneuver import Maneuver

orb_i = Orbit.circular(Earth, alt=700 << u.km)
hoh = Maneuver.hohmann(orb_i, r_f=36000 << u.km)
```

Once instantiated, `Maneuver` objects provide information regarding total $`\Delta v`$ and $`\Delta t`$:

``` pycon
>>> hoh.get_total_cost()
<Quantity 3.6173981270031357 km / s>

>>> hoh.get_total_time()
<Quantity 15729.741535747102 s>
```

`Maneuver` objects can be applied to `Orbit` instances using the `apply_maneuver` method.

``` pycon
>>> orb_i
7078 x 7078 km x 0.0 deg (GCRS) orbit
around Earth (X)

>>> orb_f = orb_i.apply_maneuver(hoh)
>>> orb_f
36000 x 36000 km x 0.0 deg (GCRS) orbit
around Earth (X)
```

### Targeting

Targeting is the problem of finding the orbit connecting two positions over a finite amount of time. Within the context of the non-perturbed two-body problem, targeting is just a matter of solving the BVP, also known as Lambert's problem. Because targeting tries to find for an orbit, the problem is included in the Initial Orbit Determination field.

The `poliastro.iod` package contains `izzo` and `vallado` modules. These provide a `lambert` function for solving the targeting problem. Nevertheless, a `Maneuver.lambert` constructor is also provided so users can keep taking advantage of `Orbit` objects.

``` python
# Declare departure and arrival datetimes
date_launch = time.Time(
    '2011-11-26 15:02', scale='tdb'
)
date_arrival = time.Time(
    '2012-08-06 05:17', scale='tdb'
)

# Define initial and final orbits
orb_earth = Orbit.from_ephem(
    Sun, Ephem.from_body(Earth, date_launch),
    date_launch
)
orb_mars = Orbit.from_ephem(
    Sun, Ephem.from_body(Mars, date_arrival),
    date_arrival
)

# Compute targetting maneuver and apply it
man_lambert = Maneuver.lambert(orb_earth, orb_mars)
orb_trans, orb_target = ss0.apply_maneuver(
    man_lambert, intermediate=true
)
```

Targeting is closely related to quick mission design by means of porkchop diagrams. These are contour plots showing all combinations of departure and arrival dates with the specific energy for each transfer orbit. They allow for quick identification of the most optimal transfer dates between two bodies.

The `poliastro.plotting.porkchop` provides the `PorkchopPlotter` class which allows the user to generate these diagrams.

``` python
from poliastro.plotting.porkchop import (
    PorkchopPlotter
)
from poliastro.utils import time_range

# Generate all launch and arrival dates
launch_span = time_range(
    "2020-03-01", end="2020-10-01", periods=int(150)
)
arrival_span = time_range(
    "2020-10-01", end="2021-05-01", periods=int(150)
)

# Create an instance of the porkchop and plot it
porkchop = PorkchopPlotter(
    Earth, Mars, launch_span, arrival_span,
)
```

Previous code, with some additional customization, generates figure `fig:porkchop`.

<figure class="align-center">
<embed src="paper_assets/porkchop.pdf" />
<figcaption>Porkchop plot for Earth-Mars transfer arrival energy showing latest missions to the Martian planet. <code class="interpreted-text" role="label">fig:porkchop</code></figcaption>
</figure>

### Plotting

For visualization purposes, poliastro provides the `poliastro.plotting` package, which contains various utilities for generating 2D and 3D graphics using different backends such as matplotlib hunter_matplotlib_2007 and Plotly inc_collaborative_2015.

Generated graphics can be static or interactive. The main difference between these two is the ability to modify the camera view in a dynamic way when using interactive plotters.

The most important classes in the `poliastro.plotting` package are `StaticOrbitPlotter` and `OrbitPlotter3D`. In addition, the `poliastro.plotting.misc` module contains the `plot_solar_system` function, which allows the user to visualize inner and outter both in 2D and 3D, as requested by users.

The following example illustrates the plotting capabilities of poliastro. At first, orbits to be plotted are computed and their plotting style is declared:

``` python
from poliastro.plotting.misc import plot_solar_system

# Current datetime
now = Time.now().tdb

# Obtain Florence and Halley orbits
florence = Orbit.from_sbdb("Florence")
halley_1835_ephem = Ephem.from_horizons(
    "90000031", now
)
halley_1835 = Orbit.from_ephem(
    Sun, halley_1835_ephem, halley_1835_ephem.epochs[0]
)

# Define orbit labels and color style
florence_style = {label: "Florence", color: "#000000"}
halley_style = {label: "Florence", color: "#84B0B8"}
```

The static two-dimensional plot can be created using the following code:

``` python
# Generate a static 2D figure
frame2D = rame = plot_solar_system(
    epoch=now, outer=False
)
frame2D.plot(florence, **florence_style)
frame2D.plot(florence, **halley_style)
```

As a result, figure `fig:plotting2D` is obtained.

<figure class="h align-center">
<img src="paper_assets/plotting_2D.png" alt="plotting_2D.png" />
<figcaption>Two-dimensional view of the inner Solar System, Florence, and Halley. <code class="interpreted-text" role="label">fig:plotting2D</code></figcaption>
</figure>

The interactive three-dimensional plot can be created using the following code:

``` python
# Generate an interactive 3D figure
frame3D = rame = plot_solar_system(
    epoch=now, outer=False,
    use_3d=True, interactive=true
)
frame3D.plot(florence, **florence_style)
frame3D.plot(florence, **halley_style)
```

As a result, figure `fig:plotting3D` is obtained.

<figure class="h align-center">
<img src="paper_assets/plotting_3D.png" alt="plotting_3D.png" />
<figcaption>Three-dimensional view of the inner Solar System, Florence, and Halley. <code class="interpreted-text" role="label">fig:plotting3D</code></figcaption>
</figure>

### Commercial Earth satellites

For satellites in low Earth orbit, the most important natural perturbations
include the first geopotential harmonic $`J_2`$ (representing the attractor's
oblateness), atmospheric drag, and higher-order geopotential harmonics. The
commercial textbook illustration cited by the original proceedings paper is
not included in this task; consult the bibliographic entry
`vallado_fundamentals_2007` in `paper_assets/refs.bib`.

At least the most significant of these perturbations need to be taken into account when propagating LEO orbits, and therefore the methods for purely Keplerian motion are not enough. As seen above, poliastro implements a number of these perturbations already - however, numerical methods are much slower than analytical ones, and this can render them unsuitable for large scale simulations, satellite conjunction assesment, propagation in constrained hardware, and so forth.

To address this issue, semianalytical propagation methods were devised that attempt to strike a balance between the fast running times of analytical methods and the necessary inclusion of perturbation forces. One of such semianalytical methods are the Simplified General Perturbation (SGP) models, first developed in hilton_mathematical_1966 and then refined in lane_improved_1969 into what we know these days as the SGP4 propagator hoots_models_1980 vallado_revisiting_2006. Even though certain elements of the reference frame used by SGP4 are not properly specified vallado_revisiting_2006 and that its accuracy might still be too limited for certain applications kelso_analysis_2009 lara_analytical_2016, it is nowadays the most widely used propagation method thanks in large part to the dissemination of General Perturbations orbital data by the US 501(c)(3) CelesTrak (which itself obtains it from the 18th Space Defense Squadron of the US Space Force).

The starting point of SGP4 is a special element set that uses Brouwer mean orbital elements brouwer_solution_1959 plus a ballistic coefficient based on an approximation of the atmospheric drag lane_improved_1969, and its results are expressed in a special coordinate system called True Equator Mean Equinox (TEME). Special care needs to be taken to avoid mixing mean elements with osculating elements, and to convert the output of the propagation to the appropriate reference frame. These element sets have been traditionally distributed in a compact text representation called Two-Line Element sets (TLEs) (see `fig:tle` for an example). However this format is quite cryptic and suffers from a number of shortcomings, so recently there has been a push to use the Orbit Data Messages international standard developed by the Consultive Committee for Space Data Systems (CCSDS 502.0-B-2).

<figure class="bht align-center">
<embed src="paper_assets/tle.pdf" />
<figcaption>Two-Line Element set (TLE) for the ISS (retrieved on 2022-06-05) <code class="interpreted-text" role="label">fig:tle</code></figcaption>
</figure>

At the moment, general perturbations data both in OMM and TLE format can be integrated with poliastro thanks to the `sgp4` Python library and the `Ephem` class as follows:

``` python
from astropy.coordinates import TEME, GCRS

from poliastro.ephem import Ephem
from poliastro.frames import Planes


def ephem_from_gp(sat, times):
    errors, rs, vs = sat.sgp4_array(times.jd1, times.jd2)
    if not (errors == 0).all():
        warn(
            "Some objects could not be propagated, "
            "proceeding with the rest",
            stacklevel=2,
        )
        rs = rs[errors == 0]
        vs = vs[errors == 0]
        times = times[errors == 0]

    cart_teme = CartesianRepresentation(
        rs << u.km,
        xyz_axis=-1,
        differentials=CartesianDifferential(
            vs << (u.km / u.s),
            xyz_axis=-1,
        ),
    )
    cart_gcrs = (
        TEME(cart_teme, obstime=times)
        .transform_to(GCRS(obstime=times))
        .cartesian
    )

    return Ephem(
        cart_gcrs,
        times,
        plane=Planes.EARTH_EQUATOR
    )
```

However, no native integration with SGP4 has been implemented yet in poliastro, for technical and non-technical reasons. On one hand, this propagator is too different from the other methods, and we have not yet devised how to add it to the library in a way that does not create confusion. On the other hand, adding such a propagator to poliastro would probably open the flood gates of corporate users of the library, and we would like to first devise a sustainability strategy for the project, which is addressed in the next section.

## Future work

Despite the fact that poliastro has existed for almost a decade, for most of its history it has been developed by volunteers on their free time, and only in the past five years it has received funding through various Summer of Code programs (SOCIS 2017, GSOC 2018-2021) and institutional grants (NumFOCUS 2020, 2021). The funded work has had an overwhemingly positive impact on the project, however the lack of a dedicated maintainer has caused some technical debt to accrue over the years, and some parts of the project are in need of refactoring or better documentation.

Historically, poliastro has tried to implement algorithms that were applicable for all the planets in the Solar System, however some of them have proved to be very difficult to generalize for bodies other than the Earth. For cases like these, poliastro ships a `poliastro.earth` package, but going forward we would like to continue embracing a generic approach that can serve other bodies as well.

Several open source projects have successfully used poliastro or were created taking inspiration from it, like spacetech-ssa by IBM[^1] or mubody bermejo_ballesteros_mubody_2022. AGI (previously Analytical Graphics, Inc., now Ansys Government Initiatives) published a series of scripts to automate the commercial tool STK from Python leveraging poliastro[^2]. However, we have observed that there is still lots of repeated code across similar open source libraries written in Python, which means that there is an opportunity to provide a "kernel" of algorithms that can be easily reused. Although `poliastro.core` started as a separate layer to isolate fast, non-safe functions as described above, we think we could move it to an external package so it can be depended upon by projects that do not want to use some of the higher level poliastro abstractions or drag its large number of heavy dependencies.

Finally, the sustainability of the project cannot yet be taken for granted: the project has reached a level of complexity that already warrants dedicated development effort that cannot be covered with short-lived grants. Such funding could potentially come from the private sector, but although there is evidence that several for-profit companies are using poliastro, we have very little information of how is it being used and what problems are those users having, let alone what avenues for funded work could potentially work. Organizations like the Libre Space Foundation advocate for a strong copyleft licensing model to convince commercial actors to contribute to the commons, but in principle that goes against the permissive licensing that the wider Scientific Python ecosystem, including poliastro, has adopted. With the advent of new business models and the ever increasing reliance in open source by the private sector, a variety of ways to engage commercial users and include them in the conversation exist. However, these have not been explored yet.

## Acknowledgements

The authors would like to thank Prof. Michèle Lavagna for her original guidance and inspiration, David A. Vallado for his encouragement and for publishing the source code for the algorithms from his book for free, Dr. T.S. Kelso for his tireless efforts in maintaining CelesTrak, Alejandro Sáez for sharing the dream of a better way, Prof. Dr. Manuel Sanjurjo Rivo for believing in my work, Helge Eichhorn for his enthusiasm and decisive influence in poliastro, the whole OpenAstronomy collaboration for opening the door for us, the NumFOCUS organization for their immense support, and Alexandra Elbakyan for enabling scientific progress worldwide.

## References

[^1]: <https://github.com/IBM/spacetech-ssa>

[^2]: <https://github.com/AnalyticalGraphicsInc/STKCodeExamples/>
