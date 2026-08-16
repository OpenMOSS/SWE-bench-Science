[J. Res. Natl. Inst. Stand. Technol. 97, 533 (1992)]

> Source: Roger B. Marks and Dylan F. Williams, "A General Waveguide Circuit
> Theory," <https://doi.org/10.6028/jres.097.024>. This NIST work is not
> subject to copyright in the United States and is republished courtesy of
> NIST. Converted from the official article to Markdown with localized images
> for offline use by SWE-bench Science on 2026-08-16. NIST does not endorse
> this conversion or benchmark.

# A General Waveguide Circuit Theory

Volume 97

Roger B. Marks and Dylan F. Williams

National Institute of Standards   
and Technology,   
Boulder, CO 80303

This work generalizes and extends the classical circuit theory of electromagnetic waveguides. Unlike the conventional theory, the present formulation applies to all waveguides composed of linear, isotropic material, even those involving lossy conductors and hybrid mode fields, in a fully rigorous way. Special attention is givcn to distinguishing the traveling waves, constructed with respect to a well-dcfined characteristic impedance, from a set of pseudo-waves, defined with respect to an arbitrary reference impedance. Matrices characterizing a linear circuit are defined, and relationships among them,

September-October 1992

some newly discovered, are derived. New ramifications of reciprocity are developed. Measurement of various network parameters is given extensive treatment.

Key words: characteristic impedance; circuit theory; microwave measurement; network analyzer; pseudo-waves; reciprocity; reference impedance; transmission line; traveling waves; waveguide.

Accepted: May 22, 1992

## Contents

1. Introduction . .. 534 3.4 Scattering and Pseudo-Scattering   
2. Theory of a Uniform Waveguide Mode 537 Matrices .. . 547   
2.1 Modal Electromagnetic Fields. . 537 3.5 The Cascade Matrix .. 548   
2.2 Waveguide Voltage and Current. 538 3.6 The Impedance Matrix. 548   
2.3 Power. 538 3.7 Change of Reference Impedance 548   
2.4 Characteristic Impedance .. 539 3.8 Multiport Reference Impedance   
2.5 Normalization of Waveguide Transformations . .. 549   
Voltage and Current ... 540 3.9 Load Impedance. 550   
2.6 Transmission Line Equivalent 4. Waveguide Metrology. . 551   
Circuit. .... 540 4.1 Measurability and the Choice   
2.7 Effective Permittivity and of Reference Impedance .... 551   
Measurement of Characteristic 4.2 Measurement of Pseudo-Waves and   
Impedance ... 543 Waveguide Voltage and Current.. 555   
3. Waveguide Circuit Theory... 543 5. Alternative Circuit Theory Using   
3.1 Traveling Wave Intensities. 543 Power Waves .... 555   
3.2 Pseudo-Waves... 544 6. Appendix A. Reduction of   
3.3 Voltage Standing Wave Ratio ... 546 Maxwell's Equations . . 556   
7. Appendix B. Circuit Parameter   
Integral Expressions ....... 557   
8. Appendix C. Relations Between   
po and γ. . . . 558   
9. Appendix D. Reciprocity   
Relations..... 559   
10. Appendix E. Relations Between   
Z and S. . . . 560   
11. Appendix F. Renormalization   
Table...... 561   
12. References 561

## 1. Introduction

Classical waveguide circuit theory, of which Refs. [1,2,3,4] are representative, proposes an analogy between an arbitrary linear waveguide circuit and a linear electrical circuit. The electrical circuit is described by an impedance matrix, which relates the normal electrical currents and voltages at each of its terminals, or ports. The waveguide circuit theory likewise defines an impedance matrix relating the waveguide voltage and waveguide current at each port. In both cases, the characterization of a network is reduced to the characterization of its component circuits. The primary caveat of waveguide circuit theory is that, at each port, a pair of identical waveguides must be joined without discontinuity and must transmit only a single mode, or at most a finite number of modes.

A great deal of confusion regarding waveguide circuits arises from the tendency to overemphasize the analogy to electrical circuits. In fact, important differences distinguish the two. For instance, the waveguide voltage and current, in contrast to their electrical counterparts, are highly dependent on definition and normalization. Also, the general conditions satisfied by the impedance matrix are different in the two cases. Furthermore, only the waveguide circuits, not electrical ones, are describable in terms of traveling waves. The latter two distinctions have been particularly neglected in the literature. In this introduction, we discuss all three of these differences and their relationship to the general waveguide circuit theory.

All waveguide circuit theories are based on some defined waveguide voltage and current. These definitions rely upon the electromagnetic analysis of a single, uniform waveguide. Eigenfunctions of the corresponding electromagnetic boundary value problem are waveguide modes which propagate in either direction with an exponential dependence on the axial coordinate. When limited to a single mode, the field distribution is completely described by a pair of complex numbers indicating the complex intensity (amplitude and phase) of these two counterpropagating traveling waves. The waveguide voltage and current, which are related to the electric and magnetic fields of the mode, are linear combinations of the two traveling wave intensities. This linear relationship depends on the characteristic impedance of the mode.

The classical definition of the waveguide voltage and current is suitable only for modes which are TE (transverse electric), TM (transverse magnetic), or TEM (transverse electromagnetic). This includes many conventional waveguides, such as lossless hollow waveguide and coaxial cable. However, modes of guides with transversely nonuniform material parameters are generally hybrid rather than TE, TM, or TEM. Thus, the classical theory is inapplicable to multiple-dielectric guides, such as microstrip, coplanar waveguide, and optical fiber waveguide. Neither does it apply to lines containing an imperfect conductor, for a lossy conductor essentially functions as a lossy dielectric. This limitation has become increasingly important with the proliferation of miniature, integrated-circuit waveguides, in which the loss is a nonnegligible factor.

In the absence of a general theory, the most popular treatment of arbitrary waveguides is based on an engineering approach (for example, Ref. [5]). The procedure makes use of the fact that, in $\mathrm { T E } ,$ TM, and TEM modes, the conventional waveguide voltage and current obey the same telegrapher's equations which govern propagation in a lowfrequency transmission line. The characteristic impedance, which enters the telegrapher's equations, can be written in terms of equivalent circuit parameters $C , G , L ,$ and R. Engineers assume that waveguide voltages and currents satisfying the telegrapher's equations continue to exist for hybrid and lossy modes. Heuristic arguments, based on low-frequency circuit theory, are used to compute the equivalent circuit parameters, and those parameter estimates are used to determine the characteristic impedance from the conventional expression.

In fact, a practical, general definition of waveguide voltage v and current i is easily constructed using methods analogous to those applied to ideal TE, TM, and TEM modes. The basic principle [1, pp. 76–77] is that, for consistency with electrical circuit theory, v and i should be related to the complex power p by $p = \nu i ^ { * }$ . This ensures that v and i are proportional to the transverse electric and magnetic fields. Reference [1] declines to further specify v and i, arguing that their ratio v/i is irrelevant and arbitrary. In fact, v/i is often pertinent. When only the forward-propagating mode exists, then ${ \pmb { \nu } } / i = { \pmb { Z } } _ { { \bf 0 } } ,$ the characteristic impedance. As pointed out by Brews [6], ${ Z _ { 0 } }$ is not entirely arbitrary; the relationship ${ p } = \nu i ^ { * }$ determines the phase of v/i and therefore of $Z _ { 0 } .$ The magnitude of $Z _ { 0 }$ is formally arbitrary, but its normalization plays a significant role in many problems. The greatest contribution of Ref. [6] is that it defines the equivalent circuit parameters in terms of the characteristic impedance, rather than vice versa, and thereby derives explicit expressions for $C , G , L ,$ and R in terms of the modal fields.

In Sec. 2 of this paper, we present a complete theory of uniform waveguide modes, beginning from first principles. We modify Brews’definition of the waveguide voltage and current with an alternate normalization devised to simplify the results. We also modify his procedure to simplify the derivation.

In Sec. 3, we proceed to develop a general waveguide circuit theory based on the results of Sec. 2. A number of conclusions presented herein are at odds with not only the electrical circuit theory but also the classical waveguide circuit theory. This is expected, for the classical theory fails to account for losses. The inadequacy of the classical waveguide circuit theory is emphasized by several surprising results of the new theory. For example, the classical theory concludes that the waveguide impedance matrix, like its counterpart in electrical circuit theory, is symmetric when the circuit is composed of reciprocal matter. Here, we demonstrate that this conclusion is not generally valid when lossy waveguide ports are allowed.

Even with the waveguide voltage and current rigorously and consistently defined and with a proper accounting of waveguide loss, another major shortcoming of the classical theory remains: the classical waveguide circuit theory fails to appreciate the subtleties of the scattering matrix, which, like the impedance matrix, characterizes the circuit, but which relates the traveling wave intensities instead of the waveguide voltages and currents. A good understanding of the scattering matrix, which is related to the impedance matrix by a one-to-one transformation based on the modal characteristic impedance, is vital to a practical waveguide circuit theory, for the scattering matrix is an essential part of an operational definition of the impedance matrix. The reason for this, as we discuss in Sec. 4, is that practical waveguide instrumentation is nearly always based on the measurement of waves or similar quantities. In contrast, waveguide voltages and currents, like the fields with which they are defined, are virtually inaccessible experimentally.

The scattering matrix provides a clear distinction between waveguide and electrical circuits, for the scattering matrix has no direct counterpart in electrical circuit theory. Electrical circuits are not subject to a traveling wave/scattering matrix description because electrical circuits are not generally composed of uniform waveguides with exponential traveling waves. This is why it is meaningless to speak of the characteristic impedance of an arbitrary electrical port. Nevertheless, the electrical circuit theory mocks the waveguide theory by introducing an arbitrary reference impedance. This parameter is used in place of the characteristic impedance in a transformation identical to that relating the corresponding waveguide parameters, resulting in analogous quantities which are often (confusingly) called "traveling waves." However, since these are not true traveling waves and possess no wave-like characteristics, we prefer to use the term pseudo-waves. The relationship between the pseudo-waves is described by a matrix, often (confusingly) called a "scattering matrix," which we instead call a pseudo-scattering matrix.

In contrast to the characteristic impedance, the reference impedance is completely arbitrary. Classical waveguide circuit theory, along with electrical circuit theory, has failed to explicitly recognize this distinction.

While the scattering matrix is incompatible with electrical circuit theory, the pseudo-scattering matrix is compatible with both waveguide and electrical theories. In this paper, we define waveguide pseudo-waves exactly as in the electrical circuit theory, using the waveguide voltage and current and an arbitrary reference impedance. These waveguide pseudo-waves cannot be interpreted as traveling waves but are a linear combination of the traveling waves.

By defining the pseudo-scattering matrix for waveguide as well as electrical circuits, we establish a description common to both. On the other hand, such a common description also exists in the form of the impedance matrix. Why do we require both impedance matrix and pseudo-scattering matrix descriptions? This question has at least three answers, which we now enumerate.

The first answer is that the commonality of the two theories allows the common use of tools developed for one of the two applications. These tools include a number of analytical theorems and results as well as a great deal of measurement and computer-aided design software. Users should be able to take advantage of tools using both impedance matrix and pseudo-scattering matrix descriptions. Furthermore, many tools require both descriptions. For example, the Smith chart connects the two in a concise and familiar way.

The second answer has to do with measurement. Electrical circuits are measured in terms of voltages and currents and are therefore fundamentally characterized by impedance matrices. In contrast, the waveguide voltage and current are related to electromagnetic fields which are rarely, if ever, subject to direct measurement. Instead, waveguide circuits are measured in terms of traveling waves and pseudo-waves. For example, a slotted line, traditionally used for waveguide circuit measurement, relies on interference between the traveling waves. Most modern waveguide measurements use a network analyzer. We show in this paper that calibrated network analyzers measure pseudo-waves, defined with respect to a reference impedance determined by the calibration. This reference impedance need not equal the characteristic impedance of the waveguide, so the measured pseudo-waves need not be the actual traveling waves.

The third reason that both impedance and pseudo-scattering descriptions are important is that both are needed to analyze the interconnection of a waveguide with an electrical circuit or with a dissimilar waveguide. Such an analysis typically makes use of two assumptions. The first is that the waveguide fields near the interconnection are composed of a single mode; this assumption may lead to an acceptable result even though the discontinuity virtually always ensures that it is inexact. The second assumption is that the (waveguide or electrical) voltage and current in that single mode are continuous at the interface. This is a generalization of a result from electrical circuit theory that is of questionable validity for waveguide circuits. Due to these two assumptions, any simple analysis of this problem is at best approximate. However, if it is to be applied, the matching conditions on the voltage and current may be directly implemented in terms of impedance parameters, while the waveguides are characterized in terms of scattering or pseudo-scattering parameters. Both sets of parameters are therefore required to solve the problem.

A good example of this kind of problem is the interconnection of a TEM or quasi-TEM waveguide with an electrical circuit which is small compared to a wavelength. In this case, the single-mode approximation may be valid, and the conventional impedance-matching method may be useful if the waveguide voltage and current are defined to be compatible with the electrical voltage and current. The canonical problem of this form is the termination of a planar, quasi-TEM waveguide, such as a microstrip line, with a small, "lumped" resistor. Such problems, while unusual in the study of conventional waveguides, are typical of planar circuits and have become increasingly important with their proliferation. The theory presented here supports the experimental study of these problems using conventional microwave instrumentation.

Although qur introduction of pseudo-waves entails some new terminology, these quantities are not new discoveries. They implicitly provide the basis of the conventional “scattering matrix" description of electrical circuit theory. Furthermore, while they have not heretofore been explicitly introduced into waveguide circuit theory, they have been applied, perhaps unconsciously, to waveguide circuits by those unaware of the distinctions between the two theories.

An important contrast to the pseudo-wave theory is an alternative known as the theory of “complex port numbers" [7]. This theory defines what it calls "traveling waves" and corresponding “scattering matrices" in a way that is fundamentally different from that described here. The theory itself was originally applied to electrical circuits and remains popular in that context. It has also been extended to waveguide analysis, where it is known as the theory of “power waves" [8]. Here we demonstrate previously-unknown properties of the “power wave scattering matrix" of a waveguide circuit. Furthermore, we show that the power waves are different from not only the pseudo-waves but also the actual traveling waves propagating in a waveguide. As a result, they present some serious complications, discussed in the text. Practitioners of the waveguide arts must be aware that conventional analysis and measurement techniques do not determine relations between power waves. Confusion concerning this matter is prevalent.

In this paper, we comprehensively construct a complete waveguide circuit theory from first principles. Beginning with Maxwell's equations in an axially independent region, we define the waveguide voltage and current, the characteristic impedance, and the four equivalent circuit parameters of the mode. We then define traveling wave intensities, which are normalized to the characteristic impedance, and pseudo-waves, which are normalized to some arbitrary reference impedance.

We discuss in detail the significance of the waves and study expressions for the power. We introduce various matrices relating the voltages, currents, and waves in the ports of a waveguide circuit and describe the properties of those matrices under typical physical conditions. We extensively investigate the problems of measuring these quantities.

Although the normalizations in many of the definitions introduced here are unfamiliar, we have striven to ensure that each parameter is defined in accordance with common usage and with the appropriate units. Awkward definitions are occasionally required to achieve convenient results.

## 2. Theory of a Uniform Waveguide Mode

In this section, we develop a basic description of a waveguide mode. Beginning with Maxwell's equations, we define the waveguide voltage and current, power, characteristic impedance, and transmission line equivalent circuit parameters. We close with a discussion of the measurement of characteristic impedance.

## 2.1 Modal Electromagnetic Fields

We begin by defining a uniform waveguide very broadly as an axially independent structure which supports electromagnetic waves. In such a geometry, we seek solutions to the source-free Maxwell equations with time dependence $e ^ { + j \omega t }$ . Here we consider only problems involving isotropic permittivity and permeability, although some of the results are easily generalized (see Appendix A). We need to prescribe the appropriate boundary conditions at interfaces and impenetrable surfaces. If the waveguide is transversely open, the region is unbounded, and boundary conditions at infinity, sufficient to ensure finite power, are also required; this excludes leaky modes. The eigenvalue problem is separable and the axial solutions are exponential. In general, there are many linearly independent solutions to this problem, each of which is proportional to a mode of the waveguide. In this paper, we restrict ourselves to consideration of a single mode which propagates in both directions. Most of the results are easily generalized to any finite number of propagating modes.

We introduce complex fields whose magnitude is the root-mean-square of the time-dependent fields, as in Ref. [9], and orient our z-axis along the waveguide axis. For a mode propagating in the forward (increasing z) direction, the normalized modal electric and magnetic fields will be denoted by $e e ^ { - \gamma z }$ and $\pmb { h e } ^ { - \pmb { \gamma } \pmb { z } } ,$ respectively, where e and h are independent of z. Although it need not be specified here, some arbitrary but fixed normalization is required to ensure uniqueness of $\pmb { e }$ and h. The modal propagation constant $\pmb { \gamma }$ is composed of real and imaginary components α and $\beta \mathrm { : }$

$$
\gamma \equiv \alpha + j \beta .\tag{1}
$$

Split e and h into their transverse (e, and ${ \pmb h } _ { t } )$ and longitudinal $( e _ { z } z$ and $h _ { z } z )$ components, where $\pmb { z }$ is the longitudinal unit vector. As shown in Appendix $\mathbf { A } ,$ the homogeneous Maxwell equations with isotropic permittivty and permeability can be expanded as

$$
\begin{array} { r } { \nabla \times \pmb { e } _ { t } = - j \omega \mu h _ { z } \pmb { z } _ { 0 } } \end{array}\tag{2}
$$

$$
\begin{array} { r } { \gamma e _ { t } + \nabla e _ { z } = - j \omega \mu z \times h _ { t } , } \end{array}\tag{3}
$$

$$
\nabla \times \boldsymbol { h } _ { t } = + j \omega \epsilon e _ { z } z \ ,\tag{4}
$$

$$
\gamma h _ { t } + \nabla h _ { z } = + j \omega \epsilon z \times e _ { t } ,\tag{5}
$$

$$
\star \nabla \cdot \boldsymbol { e } _ { t } + \boldsymbol { e } _ { t } \cdot \nabla \epsilon = \epsilon \gamma \boldsymbol { e } _ { z } \ ,\tag{6}
$$

and

$$
{ \mu } \boldsymbol { \nabla } { \cdot } \boldsymbol { h } _ { t } + \boldsymbol { h } _ { t } { \cdot } \boldsymbol { \nabla } { \mu } = { \mu } \gamma h _ { z } \ .\tag{7}
$$

We expressly exclude discussion of the case $\omega = 0 ,$ to which many of the results in this paper do not apply due to the decoupling of e and h.

To get a better understanding of the eigenvalue problem, we can eliminate either $\pmb { e _ { t } }$ or $\mathbf { { \lambda } } _ { h _ { t } }$ from Eqs. (3) and (5) and thereby derive the explicit expressions for the transverse fields in terms of the axial fields

$$
\left( \omega ^ { 2 } \mu \epsilon + \gamma ^ { 2 } \right) e _ { t } = - \gamma \nabla e _ { z } + j \omega \mu z \times \nabla h _ { z }\tag{8}
$$

and

$$
( \omega ^ { 2 } \mu \epsilon + \gamma ^ { 2 } ) h _ { t } = - \gamma \nabla h _ { z } - j \omega \epsilon z \times \nabla e _ { z } \mathrm { ~ . ~ }\tag{9}
$$

Differential equations for the axial fields are

$$
( \nabla ^ { 2 } + \omega ^ { 2 } \mu \epsilon + \gamma ^ { 2 } ) e _ { z } = \frac { \chi } { \epsilon } e _ { t } \cdot \nabla \epsilon\tag{10}
$$

and

$$
( \nabla ^ { 2 } + \omega ^ { 2 } \mu \epsilon + \gamma ^ { 2 } ) h _ { z } = \frac { \gamma } { \mu } h _ { \mathrm { t } } \cdot \nabla \mu ~ .\tag{11}
$$

These equations are in general quite complicated. In many conventional waveguides, e and $\pmb { \mu }$ are piecewise homogeneous, so the right sides of Eqs. (10) and (11) vanish. Even so, these equations remain complicated since the various fields components are coupled through the boundary conditions.

In general, the solutions of the boundary value problem possess a full suite of field components. In certain cases, it may be possible to find either a TE $( e _ { z } = 0 )$ or TM $( h _ { z } = 0 )$ solution. Equations (8) and (9) ensure that TEM $( e _ { z } = h _ { z } = 0 )$ solutions exist only in domain of homogeneous μe with the eigenvalue γ satisfying $\gamma ^ { 2 } = - \omega ^ { 2 } \mu \epsilon$ . This forbids TEM solutions in the presence of multiple dielectrics, as exist in open planar waveguides or waveguides bounded by lossy conductors.

Equations (2)-(7) prohibit nontrivial modes with either $\pmb { e _ { t } = 0 }$ or $\pmb { h } _ { t } = 0$ , except when $\gamma = 0 .$ This degenerate case, which corresponds to mode of a lossless waveguide operating at exactly the cutoff frequency, is discussed in Appendix C.

## 2.2 Waveguide Voltage and Current

Recall that $\pmb { e } _ { t _ { 1 } }$ ezz, h,, and $\displaystyle h _ { z } z$ , satisfying Eqs. $( 2 ) - ( 7 )$ with the propagation constant $^ { \mathfrak { v } , }$ represent the fields of the mode propagating in the forward direction. Clearly, the fields $e _ { t } , - e _ { z } z , - h _ { t } ,$ , and $\pmb { h } _ { z } \pmb { z }$ satisfy the same equations with a propagation constant of $- \gamma$ . These latter fields represent the normalized backward propagating mode. The distinction between the forward and backward modes is made below.

In general, the total fields E and H in a single mode of the waveguide are linear combinations of the forward and backward mode fields. Their transverse components can therefore be represented by

$$
E _ { t } = c _ { + } e ^ { - \pi } e _ { t } + c _ { - } e ^ { + \gamma z } e _ { t } \equiv \frac { v ( z ) } { v _ { 0 } } e _ { t }
$$

and

(12)

$$
H _ { t } = c _ { + } e ^ { - \tau z } h _ { t } - c _ { - } e ^ { + \tau z } h _ { t } \equiv \frac { i ( z ) } { i _ { 0 } } h _ { t } .\tag{13}
$$

We will call v and i the waveguide voltage and waveguide current. The introduction of the normalization constants v and $i _ { 0 }$ allows v and v to have units of voltage, i and $i _ { 0 }$ to have units of current, and $\mathbf { } E _ { t } , H _ { t } , e _ { t } ,$ and $\mathbf { { \lambda } } _ { h _ { t } }$ to have units appropriate to fields. Other waveguide theories omit u and in and therefore require unnatural dimensions.

For basis functions, we have chosen to use the normalized field functions $e _ { t }$ and $\mathbf { { \lambda } } _ { h _ { t } , \mathrm { ~ } }$ whereas conventional waveguide theories choose arbitrary multiples of $\pmb { e _ { t , \pmb { \imath } } }$ and $\mathbf { \lambda } _ { h _ { t } } .$ The present formulation is conceptually simpler since ${ \pmb e } _ { t }$ and $\mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathbf { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } _ { \mathbf { { \lambda } } } \mathrm { { \lambda } } \mathrm _ { \lambda } \mathrm { { \lambda } } \mathrm _ { \lambda } \mathrm { \lambda } \mathrm { { \lambda } } _ { \lambda } \mathrm \mathrm { { \lambda } } \mathrm _ { \lambda } \mathrm { \lambda } \mathrm { \lambda } _ { \lambda } \mathrm \mathrm { { \lambda } } \mathrm _ { \lambda } \mathrm { \lambda } \mathrm \mathrm { { \lambda } } \mathrm _ { \lambda } \mathrm { \lambda } \mathrm \mathrm { } \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm { \lambda } \mathrm \mathrm { } \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm \mathrm { \lambda } \mathrm \mathrm { \lambda } \mathrm \mathrm \mathrm { \lambda } \mathrm \mathrm \mathrm { \lambda \lambda } \mathrm \mathrm \mathrm { \lambda \lambda } \mathrm \mathrm \mathrm { \lambda \lambda \mathrm } \mathrm$ are the fields in the normalized forward-propagating mode. This mode has propagation constant ${ \pmb \gamma } ,$ waveguide voltage $v ( z ) { = } v _ { 0 } e ^ { - \gamma z } ,$ and waveguide current $i ( z ) = i _ { 0 } e ^ { - \gamma z }$ . For the normalized backward-propagating mode, the propagation constant is $- \gamma ,$ $v ( z ) = v _ { 0 } e ^ { + r z }$ , and $i ( z ) = - i _ { 0 } e ^ { + \gamma z } ,$

## 2.3 Power

The net complex power $p ( z )$ crossing a given transverse plane is given by the integral of the Poynting vector over the cross section S:

$$
p \left( z \right) \equiv \int _ { S } E _ { t } \times \boldsymbol { H } _ { t } ^ { * } \cdot \boldsymbol { z } \mathrm { d } S = \frac { \upsilon ( z ) i ^ { * } ( z ) } { \upsilon 0 i _ { 0 } ^ { * } } p _ { 0 } ,\tag{14}
$$

where we have defined

$$
p _ { 0 } \equiv \int _ { S } e _ { \ell } \times h _ { \ell } ^ { * } \cdot z \mathrm { d } S .\tag{15}
$$

In accordance with the analogy to electrical circuit theory, we require that

$$
p = v i ^ { * } .\tag{16}
$$

This cannot be achieved with arbitrary choices of the normalization constants vo and $i _ { 0 } .$ Therefore we impose the constraint

$$
p _ { 0 } = v _ { 0 } i _ { 0 } { } ^ { * } ,\tag{17}
$$

which allows Eqs. (14) and (16) to be simultaneously satisfied. Either $\pmb { v } _ { 0 }$ or $i _ { 0 }$ may be chosen arbitrarily; the other is determined by Eq. (17)

The magnitude of ${ p _ { 0 } }$ depends on the normalization which determined the modal fields e and $\pmb { h } ;$ in fact, Eq. (15) can even be used to specify the normalization. The phase of ${ \pmb p _ { 0 } }$ does not depend on this normalization since the phase relationship between e and h is fixed, to within a sign, by Maxwell's equations. This sign ambiguity can be resolved by explicitly distinguishing between the forward and backward modes. The most concise means of making this distinction is to define the forward mode as that in which the power flows in the +z direction; that is,

$$
\mathbf { R e } ( p _ { 0 } ) { \geqslant } 0 .\tag{18}
$$

The ambiguity remains if $\mathtt { R e } ( p _ { 0 } ) = 0 ,$ as occurs in an evanescent waveguide mode. In this case, we use the alternative condition $\mathbf { R e } ( \gamma ) { > } 0 ,$ which forces the mode to decay with z. With Eq. (18) or its alternative, the phase of ${ \pmb p _ { 0 } }$ is unambiguous, except in the degenerate case $p _ { 0 } = 0$

The average power flow $P ( z )$ across S is given by the real part of $p ( z )$ as

$$
P \left( z \right) \equiv \mathrm { R e } [ p \left( z \right) ] = \mathrm { R e } \int _ { s } E _ { t } \times H _ { t } ^ { \ast } \cdot z \mathrm { d } S = R e \left( \nu i ^ { \ast } \right) .\tag{19}
$$

When only the normalized forward mode is present, the complex power is $p ( z ) = p _ { 0 } e ^ { - 2 \alpha z }$ When only the normalized backward mode is present, the complex power is $- p _ { 0 } e ^ { + 2 \alpha z }$ . The associated average powers are $\mathbb { R e } ( p _ { 0 } ) e ^ { - 2 \alpha z }$ and $- \mathrm { R e } ( p _ { 0 } ) e ^ { + 2 \alpha z }$ , respectively. The signs differ because the forward mode carries power in the +z direction and the backward mode in the $- z$ direction.

The power is not generally a linear combination of the forward and backward mode powers, since it is given by the nonlinear expression in Eq. (19). This means that the net real power $P$ is in general not simply the difference of the powers carried by the forward and backward modes. This issue is discussed at greater length below.

## 2.4 Characteristic Impedance

We define the forward-mode characteristic impedance by

$$
Z _ { 0 } \equiv { w } / i _ { 0 } = | { w } _ { 0 } | ^ { 2 } / p _ { 0 } ^ { * } = p _ { 0 } / | i _ { 0 } | ^ { 2 } .\tag{20}
$$

The equivalence of these expressions again demonstrates the analogy to electrical circuit theory. Brews [6, 10] also defines the voltage, current, power, and characteristic impedance so as to satisfy Eq. (20) and refers to Schelkunoff's point [11] that the equivalence of these three definitions of ${ \bf \mathcal { Z } } _ { 0 }$ follows from Eq. (17). The three definitions would in general be inconsistent ${ \bf i f } p _ { 0 } , { \boldsymbol { w } } ,$ and io were defined independently (for example, in terms of some power, voltage drop, and current in the waveguide) without regard to Eq. (17).

$\scriptstyle z _ { 0 }$ is independent of the normalization of the modal fields e and h which affected |pol. While its magnitude does depend on the choice of either v or $i _ { 0 } ,$ its phase is identical to that of ${ \pmb p _ { 0 } }$ and therefore independent of all normalizations. As pointed out by Refs. [6] and [10], the phase of the characteristic impedance $\mathbf { \mathcal { Z } _ { 0 } }$ is a fixed, inherent, and unambiguous property of the mode. A sign ambiguity would have remained had we not imposed Eq. (18) since, due to the sign reversal in the current, the characteristic impedance of the backward mode is $- z _ { 0 } .$ However, Eqs. (18) and (20) constrain the sign of $\scriptstyle z _ { 0 }$ such that

$$
\mathbb { R } \mathrm { e } ( Z _ { 0 } ) \geqslant 0 .\tag{21}
$$

In particular, as we will see below, the characteristic impedance of any propagating mode of a lossless line is real and positive. Equation (21) serves to completely specify $\scriptstyle z _ { 0 }$ unless $\mathbb { R e } ( Z _ { 0 } ) = 0 ;$ in which case the alternative condition $\mathtt { R e } ( \gamma ) > 0$ suffices to make the distinction.

When only a multiple of the forward-propagating mode exists, then $\nu ( \bar { z } ) / i ( z ) = Z _ { 0 }$ for all z and at any amplitude. Likewise, when only a multiple of the backward mode exists, then $\nu ( z ) / i ( z ) = - \bar { Z } _ { 0 } .$ If both forward and backward modes are present, v/i depends on z due to interference between the two.

In order to illustrate the close correspondence between this definition of $\scriptstyle { Z _ { 0 } }$ and conventional definitions of the characteristic impedance, we consider the special case of TE, TM, or TEM modes in homogeneous matter. Each of these has fields which satisfy

$$
\begin{array} { r } { z \times e _ { t } = \eta h _ { t } , } \end{array}\tag{22}
$$

where the wave impedance η is constant over the cross section. In this case,

$$
Z _ { 0 } = \frac { | \upsilon _ { 0 } | ^ { 2 } } { \int _ { S } | e _ { t } | ^ { 2 } \mathrm { d } S } \ \eta .\tag{23}
$$

Since the modal field $\pmb { e _ { t } }$ is normalized, the denominator is fixed. The magnitude of $\scriptstyle z _ { 0 }$ therefore depends only on vo. However, the phase $o f$ the characteristic impedance is equal to that of the wave impedance. This corresponds to most conventional definitions.

For TEM modes, η is equal to the intrinsic wave impedance $\sqrt { \mu / \epsilon } ( \approx 3 7 7$ Ω in free space), with the result that

$$
\arg ( Z _ { 0 } ) = \frac { 1 } { 2 } \big ( \arg ( \mu ) - \arg ( \epsilon ) \big ) .\tag{24}
$$

For example, if $\pmb { \mu }$ is real then

$$
\arg ( Z _ { 0 } ) = - \frac { 1 } { 2 } \delta ,\tag{25}
$$

where tan $\delta \equiv \mathrm { I m } ( \epsilon ) / \mathrm { R e } ( \epsilon )$ is the dielectric loss tangent.

When v is chosen to be the voltage between the ground and signal conductors, $\scriptstyle z _ { 0 }$ is equal to the conventional TEM characteristic impedance.

For TE and TM modes,

$$
\eta = \sqrt { \frac { \mu } { \epsilon } } \Bigl ( 1 - { \frac { k _ { \mathrm { c } } ^ { 2 } } { \omega ^ { 2 } \mu \epsilon } } \Bigr ) ^ { \pm 1 / 2 } ,\tag{26}
$$

where $^ { 6 6 } + { } ^ { , 9 }$ corresponds to TM and $^ { \mathfrak { t } \mathfrak { t } } - ^ { \mathfrak { p } }$ to TE and $\pmb { k } _ { \mathbf { c } }$ is the cutoff wavenumber.

## 2.5 Normalization of Waveguide Voltage and Current

Although the phase of either v or $\dot { \iota } _ { 0 }$ can be chosen arbitrarily, the choice is of little significance. The important quantity is the phase relationship between v and $i _ { 0 } ,$ which, due to the constraint (17) and the fact that the phase of ${ \pmb p } _ { \pmb 0 }$ is fixed, is unalterable. The phase relationship between $\pmb { \nu _ { 0 } }$ and $i _ { 0 }$ is a unique property of the mode.

The magnitude of $Z _ { 0 }$ is determined by the choice of v or $i _ { 0 } .$ Given the constraint $[ ( \mathbf { E q . 1 7 } ) ] ,$ and having selected a modal field normalization, we may independently assign only one of these two variables. One useful normalization defines the constant u by analogy to a voltage using the path integral

$$
\boldsymbol { v } _ { 0 } = - \int _ { \mathrm { p a t h } } \boldsymbol { e } _ { t } \cdot \mathrm { d } \boldsymbol { l } .\tag{27}
$$

The path is confined to a single transverse plane with the restriction that $\mathbf { \nabla } \mathbf { u } _ { 0 } { \neq } \mathbf { 0 } .$ This can always be arranged unless $\mathbf { \nabla } . \pmb { \theta } _ { t } = \mathbf { 0 }$ everywhere, but this occurs only in the degenerate case $\pmb { \gamma } = \pmb { 0 }$ The integral does not in general represent a potential difference because it depends on the path between a given pair of endpoints. In certain cases, such as when the mode is TM or TEM, the integral depends only on the endpoints, not on the path between them.

Although the path is arbitrary, certain choices are often natural. With a TEM mode, for example, we can put an endpoint on each of two active conductors so that $\pmb { \nu _ { 0 } }$ becomes the path-independent voltage drop across them at ${ \pmb z } = { \bf 0 }$ in the normalized mode. In this case, $\scriptstyle z _ { 0 }$ is equal to the conventional TEM characteristic impedance. We may not have both endpoints on the same conductor, for then ${ \mathfrak { v } } _ { 0 } = 0 .$ The same is true of TM modes.

A result of Eq. (27) is that v is also analogous to voltage:

$$
\nu ( z ) = - \int _ { \mathrm { p u t h } } \boldsymbol { E } _ { \iota } ( z ) \cdot \mathrm { d } \boldsymbol { l } \ .\tag{28}
$$

The normalization in Eq. (27) yields what is known as a “power-voltage" definition of the characteristic impedance, even though the "voltage" is not an actual potential difference. Another useful possibility is a “power-current" definition, choosing $i _ { 0 }$ to be a current. Yet another choice, popular for hollow waveguides, is to normalize so that $| Z _ { 0 } | = 1$ . It is not our intent to debate the issue of the optimal definition. However, it is only the magnitude, not the phase, of $\scriptstyle z _ { 0 }$ that is open for discussion.

A "voltage-current" definition, popular in the literature, is generally forbidden by Eq. (20), since an arbitrarily specified ${ \bf { \sigma } } _ { \bf { { u } } }$ and $i _ { 0 }$ may not be of the appropriate phase to satisfy $v _ { 0 } / i _ { 0 } = Z _ { 0 } .$

Appendix $\mathbf { F }$ includes a table displaying the effects of renormalizing ${ \pmb v } _ { 0 }$ and $\curvearrowleft$ on all of the parameters used in this work.

## 2.6 Transmission Line Equivalent Circuit

We now develop a transmission line analogy by defining real equivalent circuit parameters $c , L ,$ $G ,$ and $\pmb { R }$ , analogous to the capacitance, inductance, conductance, and resistance per unit length of conventional transmission line theory. The four parameters are defined by

$$
j \omega C + G \equiv \frac { \gamma } { Z _ { 0 } }\tag{29}
$$

and

$$
j \omega L + R \equiv \gamma Z _ { 0 } .\tag{30}
$$

Equations (29) and (30) are identical to those derived from the electrical circuit theory description of a transmission line with distributed shunt admittance $j \omega C + G$ and series impedance $j \omega L + R$ as shown in Fig. 1. These quantities also appear in the conventional transmission line equations satisfied by v and i:

$$
\frac { \mathrm { d } \upsilon } { \mathrm { d } z } = - \left( j \omega L + R \right) i\tag{31}
$$

and

$$
\frac { \mathrm { d } i } { \mathrm { d } z } = - ( j \omega C + G ) \nu .\tag{32}
$$

![](images/09ba579ba9a2ffc6b05525d37fbdc519a8fcd6140d08cf17cb8a4220eafa9903.jpg)  
Fig. 1. Equivalent circuit model of transmission line.

Although Eqs. (29) and (30) provide unique definitions of the four circuit parameters, it is possible to cast them into another form which is more convenient for many purposes, as is done by Brews [6]. A simpler derivation, given in Appendix B, shows that the circuit parameters are given exactly by

$$
C = \frac { 1 } { \vert \boldsymbol { \upsilon } _ { 0 } \vert ^ { 2 } } \left[ \int _ { S } \boldsymbol { \epsilon } ^ { \prime } \vert \boldsymbol { e } _ { t } \vert ^ { 2 } \mathrm { d } S - \int _ { S } \boldsymbol { \mu } ^ { \prime } \vert h _ { z } \vert ^ { 2 } \mathrm { d } S \right] ,\tag{33}
$$

$$
L = \frac { 1 } { \left. i _ { 0 } \right. ^ { 2 } } \left[ \int _ { S } \mu ^ { \prime } \left. h _ { \mathrm { t } } \right. ^ { 2 } \mathrm { d } S - \int _ { S } \epsilon ^ { \prime } \left. e _ { z } \right. ^ { 2 } \mathrm { d } S \right] ,\tag{34}
$$

$$
G = \frac { \omega } { | \nu _ { 0 } | ^ { 2 } } \left[ \int _ { S } \epsilon ^ { \prime \prime } | e _ { t } | ^ { 2 } \mathrm { d } S + \int _ { S } \mu ^ { \prime \prime } | h _ { z } | ^ { 2 } \mathrm { d } S \right] ,\tag{35}
$$

and

$$
R = \frac { \omega } { | i _ { 0 } | ^ { 2 } } \left[ \int _ { S } \mu ^ { \prime \prime } | h _ { t } | ^ { 2 } \mathrm { d } S + \int _ { S } \epsilon ^ { \prime \prime } | e _ { z } | ^ { 2 } \mathrm { d } S \right] .\tag{36}
$$

Here $\pmb { \epsilon } \equiv \pmb { \epsilon } ^ { \prime } - j \pmb { \epsilon } ^ { \prime \prime }$ and $\mu \equiv \mu ^ { \prime } - j \mu ^ { \prime \prime }$ . In passive media, the four real components $\epsilon ^ { \prime } , \epsilon ^ { \prime \prime } , \mu ^ { \prime } ;$ and $\mu ^ { \prime \prime }$ are all nonnegative. Metal conductivity is not included as an explicit term in $\pmb { \epsilon }$ but is instead absorbed in $\epsilon " .$ In general, of course, € and $\pmb { \mu }$ depend on $\pmb { \omega } .$

The parameters C, L, G, and R depend on the same normalization that determines the magnitude of $\scriptstyle z _ { 0 } .$ For instance, when ${ \pmb v } _ { 0 }$ is chosen to be the voltage between two active conductors in a lossless TEM line, then $c$ and L are the conventional capacitance and inductance per unit length. Certain combinations of these parameters, notably G/(ωC), R/(ωL), RC, RG, LC, and LG, are normalization-independent.For example, $L C = \epsilon ^ { \prime } \mu ^ { \prime }$ for a TEM line.

Equations (33) through (36) have many applications. In addition to providing a means of numerically calculating the circuit parameters from known fields, they offer opportunities for analytical calculations and approximations as well. The quadratic form in which the fields appear make them particularly useful for these purposes. Another major role they serve is in the attribution of circuit-parameter components to portions of the cross section. For example, it is common to divide the inductance L into an “external" inductance in the dielectric and an"internal" inductance in the imperfect metal. Such a division cannot be undertaken using only Eq. (30) but is readily obtainable by dividing the surface integral in Eq. (34) into dielectric and metal regimes.

Equations (29) and (30) imply the familiar expressions

$$
\gamma = \sqrt { \left( j \omega L + R \right) \left( j \omega C + G \right) }\tag{37}
$$

and

$$
Z _ { 0 } = \sqrt { ( j \omega L + R ) / ( j \omega C + G ) } .\tag{38}
$$

The pairs of roots in Eqs. (37) and (38) correspond to the presence of both forward and backward modes, each of which have identical $c , L , G$ , and $\pmb R$ but opposite $\pmb { \gamma }$ and $\scriptstyle z _ { 0 } .$ To distinguish the two, recall from Eq. (21) that the forward mode is defined such that $\mathtt { R e } ( Z _ { 0 } ) \geqslant 0$ . Either Eq. (29) or (30) can then be used to distinguish between the two values of $\pmb { \gamma } .$ If the waveguide material is passive, then Eqs. (35) and (36) ensure that $\pmb { G }$ and R are both nonnegative, which requires that $\alpha \equiv \mathrm { R e } ( \gamma ) \geq 0$ Thus, the fields of the mode that we have defined as the forward one' must decay with increasing z in a lossy system. In general, however, the sign of α does not distinguish the forward and backward modes since ${ \pmb { \alpha } } = { \bf 0 }$ in energy-conserving modes and may be negative in the presence of active media. Nevertheless, Eq. (18) ensures that the forward mode carries power only in the +z direction.

C and $\pmb { L }$ are typically positive for modes of common interest, in which the energy is primarily carried in the transverse fields and the second integrals of Eqs. (33) and (34) are relatively small. On the other hand, C and L may be zero or negative in certain cases. For instance, in the lossless case in which $\epsilon ^ { \prime \prime } { = } \mu ^ { \prime \prime } { = } 0 , G { = } R { = } 0$ and Eqs. (37) and (38) become

$$
( \epsilon ^ { \prime \prime } = \mu ^ { \prime \prime } = 0 ) \Rightarrow \gamma = j \omega \sqrt { L C }\tag{39}
$$

and

$$
( \epsilon ^ { \prime \prime } = \mu ^ { \prime \prime } = 0 ) \Rightarrow Z _ { 0 } = \sqrt { \frac { L } { C } }\tag{40}
$$

As shown in Appendix C, the modes of a lossless waveguide, except those with ${ p } _ { 0 } = 0 ;$ either propagate without attenuation $( \alpha \equiv \mathrm { R e } ( \gamma ) = 0 )$ or are evanescent $( \pmb { \alpha } > 0$ but $\beta \equiv \mathrm { I m } ( \gamma ) = 0 )$ . For the propagating modes, therefore, $_ { L C }$ is nonnegative and thus $\scriptstyle { Z _ { 0 } }$ and $p _ { 0 }$ are real. For the evanescent modes, $Z _ { 0 }$ and $p _ { 0 }$ are imaginary and the mode carries no average real power. Equation (39) shows that, for evanescent modes, either L or $^ { c , }$ but not both, must be negative. For instance, TM modes have $h _ { z } = 0 _ { : }$ so that $c$ cannot be negative. As a result, $L > 0$ for propagating TM modes and $L < 0$ for evanescent TM modes. Complementary statements hold for lossless TE modes.

In lossy waveguides, we can no longer strictly distinguish “propagating" from “evanescent" modes, since generally α and $\beta$ are both nonzero. Therefore, if we perturb a lossless TM mode by the addition of a minuscule amount of $\epsilon ^ { \prime \prime } ,$ we find a mode that is not evanescent in a strict sense (since $\beta \neq 0 )$ but nevertheless has $L < 0 ,$ In this way we prove that not all modes with $L < 0$ or $c < 0$ are strictly evanescent.

The allowed range of the phases of $\pmb { \gamma }$ and $\scriptstyle { Z _ { 0 } }$ is determined by Eqs. (37) and (38). We assume for the moment that G and R are nonnegative, as in passive structures. In this case, if $c$ and $L$ are positive, then $\pmb { \gamma }$ lies in the first quadrant and $- 4 5 ^ { \circ } \leqslant$ $\arg ( Z _ { 0 } ) \leqslant 4 5 ^ { \circ }$ . If in addition $G = 0 ,$ a good approximation in many common quasi-TEM waveguides, then $4 5 ^ { \circ } \leqslant \arg ( \gamma ) \leqslant 9 0 ^ { \circ }$ and $- 4 5 ^ { \circ } \leqslant \arg ( Z _ { 0 } ) \leqslant 0 ^ { \circ }$ If instead $R = 0 ;$ then again $4 5 ^ { \circ } \leqslant \arg ( \dot { \gamma } ) \leqslant 9 0 ^ { \circ }$ , but now $0 ^ { \circ } \leqslant \arg ( Z _ { 0 } ) \leqslant 4 5 ^ { \circ }$ In lossless propagating modes, $\pmb { \gamma }$ is positive imaginary and $\scriptstyle { Z _ { 0 } }$ positive real. $\scriptstyle { Z _ { 0 } }$ is also real in lossy lines in the special case $G / ( \omega C ) = R / ( \omega L )$

Figures (2) and (3) illustrate the allowed range of the phase of $\scriptstyle { Z _ { 0 } }$ and $\pmb { \gamma }$ for various cases, as distinguished by the signs of L and C. G and R are assumed nonnegative in these figures.

Let us compare the current results to the conventional theory of TEM lines. For a lossless TEM line, $\pmb { G }$ and R vanish, as do the second integrals in $c$ and $L$ The remaining integrals in $c$ and $L$ are simply the energy per unit length stored in the electric and magnetic fields, respectively. Thus the expressions for $c$ and $L$ are simply the conventional expressions for the dc capacitance and inductance per unit length, as given by Collin [3]. When the dielectric is lossy but $\mu ^ { \prime \prime }$ is zero, the mode may remain TEM but a shunt conductance $\pmb { G }$ , given by the first term of Eq. (35) as in Ref. [3], is present.

For a general TEM line,

$$
( \mathrm { T E M } ) \colon \ : Z _ { 0 } ^ { 2 } = \frac { \epsilon ^ { \prime } \mu } { \epsilon \mu ^ { \prime } } \frac { L } { C } = \frac { \mu } { \mu ^ { \prime 2 } \epsilon } L ^ { 2 } = \frac { \mu \epsilon ^ { \prime 2 } } { \epsilon } \frac { 1 } { C ^ { 2 } } ,\tag{41}
$$

which takes a more familiar form when $\epsilon ^ { \prime \prime } { = } \mu ^ { \prime \prime } { = } 0 .$

When the metal boundaries are lossy or the dielectric is inhomogeneous, the mode is non-TEM. The second integrals in $c$ and $L$ , which are absent in Ref. [3], are quadratic in the longitudinal fields and may, in some quasi-TEM cases, prove to be negligible compared to the first terms. The expressions for $c$ and $\pmb { G }$ in general include contributions due to fields inside the metal that are not often appreciated. A nonzero series resistance $R ,$ given by the second integral in Eq. (36), may also appear whenever $\scriptstyle e _ { z }$ and $\pmb { \epsilon } ^ { \prime \prime }$ are nonzero; the integral extends over a lossy dielectric as well as an imperfect conductor. Collin does not provide a surface-integral expression for R, but it can be shown that Eq. (36) reduces to Collins line-integral expression when the surface-impedance approximation is invoked and the dielectric is lossless.

![](images/6c62964a3c08d0a8affa771cadf95d588e955dcedecd9ffce7b269e7573b6d2c.jpg)  
Fig. 2. Allowed ranges of the phase of $Z _ { 0 }$ for various signs of the equivalent circuit parameters. The figure gives no indication of the magnitude of ${ \dot { Z } } _ { 0 } . G$ and $R$ are assumed to be nonnegative.

![](images/a7373d08e6987b9bd75ca49f52a9084228da68456bfccbca153b31bf1aefdfad.jpg)  
Fig. 3. Allowed ranges of the phase of $\pmb { \gamma }$ for various signs of the equivalent circuit parameters. The figure gives no indication of the magnitude of $\pmb { \gamma } .$ G and R are assumed to be nonnegative.

## 2.7 Effective Permittivity and the Measurement of Characteristic Impedance

It is useful and customary to define the effective relative dielectric constant (or permittivity) by

$$
\epsilon _ { \mathrm { r , e f f } } \equiv - ( c \gamma / \omega ) ^ { 2 } .\tag{42}
$$

where c is the speed of light in vacuum. This definition equates $\pmb { \gamma }$ to the propagation constant of a TEM mode in a fictitious medium of permittivity $\epsilon _ { \mathrm { r , e f f } }$ €0 and permeability $\mu _ { 0 } .$ We have no need to define an effective permeability.

Using Eq. (37),

$$
\epsilon _ { \mathrm { r , e f f } } = \frac { c ^ { 2 } } { \omega ^ { 2 } } [ \omega ^ { 2 } L C - R G - j \omega ( L G + R C ) ] .\tag{43}
$$

$\mathbf { I f } ,$ as is most common, $c , L , G$ , and R are nonnegative, then Im $( \epsilon _ { \mathrm { r , e f f } } ) \leqslant 0 .$ Although $\scriptstyle \mathrm { { R e } } ( \epsilon _ { \mathrm { r } , \mathrm { e f f } } )$ is typically positive, it becomes negative in lossy lines at low frequencies if $R G > \omega ^ { 2 } L \stackrel {  } { C }$ . It is also negative for lossless, evanescent modes.

An alternative form of Eq. (29) is

$$
Z _ { 0 } = \frac { \sqrt { \epsilon _ { \mathrm { r , e f f } } } } { c C ( 1 + G / _ { j \omega C } ) } ,\tag{44}
$$

which, as discussed in Ref. [12], may be applicable to the determination of $Z _ { 0 } .$ For example, if $G / ( \omega C )$ is known, the phase of $\scriptstyle z _ { 0 }$ is determined by the phase of $\epsilon _ { \mathrm { r , e f f } } .$ For TM modes in homogeneous dielectric, $G / ( \omega C ) = \tan \delta$ , which is typically much less than 1 and can often be neglected. The same is true for typical quasi-TEM modes. In these cases, $c$ is nearly independent of frequency and may be readily determinable [13]. If ${ \mathfrak { s o } } ,$ then Eq. (44) provides the magnitude as well as the phase of $\scriptstyle z _ { 0 } .$ This provides a practical method of determining $z _ { \infty }$ since $\epsilon _ { \mathrm { r } , \mathrm { e f f } }$ may be readily measured using standard microwave instrumentation to measure $\pmb { \gamma } .$ By contrast, a direct measurement of $Z _ { 0 }$ is impractical. For instance, the phase of ${ \cal Z } _ { 0 }$ is defined as the phase of the complex power ${ p } _ { 0 } ,$ a quantity which is difficult to assess directly without detailed knowledge of the modal fields.

A similar method of determining $Z _ { 0 }$ makes use of the relationship between $\scriptstyle { Z _ { 0 } , }$ γ, $L$ , and R described by Eq. (30). This method is often difficult to apply, particularly at low frequencies in the presence of lossy conductors, whose internal inductance and resistive loss typically make $R / ( \omega L )$ nonnegligible and $L$ and R strongly dependent on resistivity and frequency. In other cases, however, it may prove useful.

## 3. Waveguide Circuit Theory

In this section, we apply the results of Sec. 2 to develop a waveguide circuit theory. We first discuss traveling waves and pseudo-waves for a single uniform waveguide. These form the basis of the scattering and pseudo-scattering matrices. We also introduce the cascade and impedance matrices and discuss the transformation of reference impedance, concluding with an investigation of the load impedance.

## 3.1 Traveling Wave Intensities

We define the forward and backward traveling wave intensities (or simply traveling waves) ${ \pmb a } _ { \mathbf { 0 } }$ and $b _ { 0 }$ by normalizing the forward and backward modes of Eqs. (12) and (13):

$$
a _ { 0 } \equiv \sqrt { \mathrm { R e } ( p _ { 0 } ) } c _ { + } e ^ { - \gamma z } = \frac { \sqrt { \mathrm { R e } ( p _ { 0 } ) } } { 2 \upsilon _ { 0 } } \left( \upsilon + i Z _ { 0 } \right)\tag{45}
$$

and

$$
b _ { 0 } \equiv \sqrt { \mathrm { R e } ( p _ { 0 } ) } \ c _ { - } e ^ { + \gamma z } = \frac { \sqrt { \mathrm { R e } ( p _ { 0 } ) } } { 2 \upsilon _ { 0 } } ( \upsilon - i Z _ { 0 } ) ,\tag{46}
$$

where the positive square root is mandated. This power normalization ensures that, in the absence of the backward wave, the unit forward wave with $\scriptstyle { a _ { 0 } = 1 }$ carries unit power.

It can be shown that ${ \pmb a } _ { 0 }$ and ${ \pmb b _ { 0 } }$ are independent of the arbitrary normalization of $v _ { 0 } .$ While their phases depend on the phase of the modal field $\pmb { e _ { t } }$ in the same way that $c _ { + }$ and $c _ { - } \ \mathtt { d o } ,$ a0 and ${ \pmb b } _ { 0 }$ are independent of the magnitude of e. This normalization-independence suggests that ao and $b _ { 0 }$ are physical waves rather than simply mathematical artifacts.

Assuming that $\begin{array} { r } { \mathbf { R e } ( Z _ { 0 } ) { \neq } 0 , } \end{array}$ Eqs. (45) and (46) imply

$$
\upsilon ( z ) = \frac { \upsilon _ { 0 } } { \sqrt { \mathrm { R e } ( p _ { 0 } ) } } \left( a _ { 0 } + b _ { 0 } \right)\tag{47}
$$

and

$$
i ( z ) = \frac { i _ { 0 } } { \sqrt { \mathrm { R e } ( p _ { 0 } ) } } ( a _ { 0 } - b _ { 0 } ) .\tag{48}
$$

From Eq. (19), the real power is therefore

$$
P ( z ) = | a _ { 0 } | ^ { 2 } - | b _ { 0 } | ^ { 2 } + 2 \ \mathrm { I m } ( a _ { 0 } { b _ { 0 } } ^ { * } ) \frac { \mathrm { I m } ( Z _ { 0 } ) } { \mathrm { R e } ( Z _ { 0 } ) } .\tag{49}
$$

This demonstrates that the net real power $\pmb { P }$ crossing a reference plane is not equal to the difference of the powers carried by the forward and backward waves acting independently, except when the characteristic impedance is real or when either ao or $b _ { 0 }$ vanishes.

Although Eq. (49) is awkward and somewhat counterintuitive, it is not an artifact of the formulation but an expression of fundamental physics. Normalizations do not play a role, for the result is independent of the normalizations of $\cdot _ { e _ { t } }$ and $\pmb { \nu _ { 0 } } .$ Only the phase of $Z _ { 0 }$ appears and, as we have seen, this phase is not arbitrary.

In the evanescent case, $\begin{array} { r } { \mathbf { R e } ( p _ { 0 } ) = \mathbf { R e } ( Z _ { 0 } ) = 0 , } \end{array}$ so that neither the forward nor backward wave individually carries real power. In this case, Eq. (49) is indeterminate. To resolve the problem, we can express Eq. (49) in the form

$$
P ( z ) = | a _ { 0 } | ^ { 2 } - | b _ { 0 } | ^ { 2 } + 2 \mathrm { I m } ( p _ { 0 } ) \mathrm { I m } ( c _ { + } c _ { - } { } ^ { * } ) ,\tag{50}
$$

since $\beta = 0$ for evanescent waves. When $\mathtt { R e } ( p _ { 0 } ) = 0 _ { : }$ both ${ \pmb a } _ { 0 }$ and $b _ { 0 }$ vanish as a result of the power normalization of Eqs. (45) and (46), but the last term may be nonzero. This means, that, although the forward and backward cutoff waves each carry no real power, power may be transferred if both waves exist. Thus, as we expect, power may traverse a finite length of lossless waveguide in which all modes are strictly cut off. This familiar case exemplifies the fact that the net power may fail to equal the sum of the individual wave powers.

The reflection coefficient $\scriptstyle { { \cal { T } } _ { 0 } }$ is defined by

$$
\begin{array} { r } { { \cal { T } } _ { 0 } ( z ) \equiv \frac { b _ { 0 } ( z ) } { a _ { 0 } ( z ) } . } \end{array}\tag{51}
$$

The power can be expressed in terms of $\boldsymbol { { \cal T } _ { 0 } }$ by

$$
P = | a _ { 0 } | ^ { 2 } \biggl [ 1 - | I _ { 0 } | ^ { 2 } - 2 \mathrm { I m } ( { \cal T } _ { 0 } ) \frac { \mathrm { I m } ( Z _ { 0 } ) } { \mathrm { R e } ( Z _ { 0 } ) } \biggr ] ,\tag{52}
$$

which is similar to a result on $\mathbf { p } .$ 27 of Ref. [2]. As noted in Ref. [2], $| { \cal T } _ { 0 } ^ { 2 }$ is not a power reflection coefficient and may exceed 1 if $Z _ { 0 }$ is not real.

## 3.2 Pseudo-Waves

We now introduce another set of parameters, the pseudo-waves, which, in contrast to the traveling waves, are mathematical artifacts but may have convenient properties. ${ \bf W } \mathbf { e }$ first introduce an arbitrary reference impedance $Z _ { \mathrm { r e f } _ { 3 } }$ with the sole stipulation $\mathrm { R e } ( Z _ { \mathrm { r e f } } ) \geq 0$ We then define the complex pseudowave amplitudes (or simply pseudo-waves) a and b by

$$
a \left( Z _ { \mathrm { r e f } } \right) \equiv \left[ \begin{array} { l } { \frac { \left| \boldsymbol { v } _ { 0 } \right| } { \upsilon _ { 0 } } \frac { \sqrt { \mathrm { R e } \left( Z _ { \mathrm { r e f } } \right) } } { 2 \left| Z _ { \mathrm { r e f } } \right| } } \end{array} \right] \left( \upsilon + i Z _ { \mathrm { r e f } } \right)\tag{53}
$$

and

$$
b ( Z _ { \mathrm { r e f } } ) \equiv \biggl [ \frac { | { \boldsymbol { v } } _ { 0 } | } { u _ { 0 } } \frac { \sqrt { \mathrm { R e } ( Z _ { \mathrm { r e f } } ) } } { 2 | Z _ { \mathrm { r e f } } | } \biggr ] ( \upsilon - i Z _ { \mathrm { r e f } } ) .\tag{54}
$$

Although a and b depend on z (through v and i), we have chosen not to explicitly list z as an argument but instead to concentrate on the parameter $Z _ { \mathrm { r e f } } ,$ which plays a more important role in the remainder of this development.

The inverse relationships to Eqs. (53) and (54) are

$$
\upsilon = \left[ \frac { \upsilon _ { 0 } } { \vert \upsilon _ { 0 } \vert } \frac { \vert Z _ { \mathrm { r e f } } \vert } { \sqrt { \mathrm { R e } ( Z _ { \mathrm { r e f } } ) } } \right] \left( a + b \right)\tag{55}
$$

and

$$
i = \frac { 1 } { Z _ { \mathrm { r e f } } } \left[ \frac { { \upsilon } _ { 0 } } { \left| { \upsilon } _ { 0 } \right| } \frac { \left| Z _ { \mathrm { r e f } } \right| } { \sqrt { \mathrm { R e } ( Z _ { \mathrm { r e f } } ) } } \right] ( a - b ) .\tag{56}
$$

Positive square roots are again mandated in Eqs.   
(53) through (56).

With these definitions, Eq. (19) becomes

$$
P = \{ a \} ^ { 2 } - | b | ^ { 2 } + 2 \operatorname { I m } ( a b ^ { * } ) \frac { \operatorname { I m } ( Z _ { \mathrm { r e f } } ) } { \operatorname { R e } ( Z _ { \mathrm { r e f } } ) } .\tag{57}
$$

$P , \upsilon ,$ and i were defined earlier and do not depend on $Z _ { \mathrm { r e f } } .$

The pseudo-reflection coefficient Γ, defined by

$$
\Gamma ( Z _ { \mathrm { r e f } } ) \equiv _ { a ( Z _ { \mathrm { r e f } } ) } ^ { b ( Z _ { \mathrm { r e f } } ) } ,\tag{58}
$$

depends on $Z _ { \mathrm { r e f } } .$ The analog of Eq. (52) is

$$
P = | a | ^ { 2 } \left[ 1 - | I | ^ { 2 } - 2 \mathrm { I m } ( I ) \frac { \mathrm { I m } ( Z _ { \mathrm { r e f } } ) } { \mathrm { R e } ( Z _ { \mathrm { r e f } } ) } \right] .\tag{59}
$$

Comparing Eqs. (45) and (46) with Eqs. (53) and (54), we see that $a ( Z _ { 0 } ) = a _ { 0 }$ and $\begin{array} { r } { b ( Z _ { 0 } ) = b _ { 0 } . } \end{array}$ Although the multiplicative factor in Eqs. (53) and (54) is complicated, it is the only factor that satisfies this criterion and also ensures that a and b satisfy the simple power expression Eq. (57).

Since the pseudo-waves are equivalent to the actual traveling waves when the reference impedance is equal to the characteristic impedance of the mode, this is the natural choice of reference impedance. On the other hand, it is not always the most convenient choice. For instance, when $Z _ { 0 }$ varies greatly with frequency, as is often the case in lossy lines [12], the resulting measurements using ${ Z _ { \mathrm { r e f } } } = { Z _ { 0 } }$ may be difficult to interpret; a constant $Z _ { \mathrm { r e f } }$ may be preferable. Furthermore, the characteristic impedance of a given mode is often unknown and difficult to measure. In such cases, the fact that $Z _ { \mathrm { r e f } } = Z _ { 0 }$ does not suffice to provide a numerical value for $Z _ { \mathrm { r e f } } ,$ which is required in order to make use of Eqs. (55) through (57).

Other choices of reference impedance are also well motivated. In particular, if $Z _ { \mathrm { r e f } }$ is chosen to be real, the crossterm in Eq. (57) disappears. The result is the conventional expression in which the power is simply the difference of $| a | ^ { 2 }$ and $| b | ^ { 2 }$ . The choice of real $Z _ { \mathrm { r e f } }$ therefore simplifies subsequent calculations and allows the application of a number of standard results which arise from the conventional expression. For example, conservation of energy ensures that the net power P into a passive load is nonnegative. If $Z _ { \mathrm { r e f } }$ is real, Eq. (59) implies that the load's reflection coefficient has magnitude less than $^ { 1 ; }$ that is, it "stays inside the Smith chart." This need not be true for complex $Z _ { \mathrm { r e f } } .$ Another example is the conventional result that the maximum power available from a generator is that power which would be delivered to a load whose reflection coefficient is the complex conjugate of the generators reflection coefficient. In the general case, this result applies only to pseudo-reflection coefficients using a real reference impedance.

One more choice of reference impedance is in common use: that which makes $ { b ( Z _ { \mathrm { r e f } } ) }$ vanish at a given point on the line. Such a choice $( Z _ { \mathrm { r e f } } = \upsilon / i )$ also simplifies Eq. (57), although only at the particular z and for a particular termination.The primary effect of this choice of $Z _ { \mathrm { r e f } }$ is to make the pseudo-reflection coefficient vanish. As discussed later in this paper, many calibration schemes force the pseudoreflection coefficient of some “standard" termination, usually a resistive load, to vanish. Those schemes thereby implicitly impose this particular choice of reference impedance.

Unfortunately, the quantities a and b are proportional to the forward and backward traveling waves only if $\boldsymbol { Z } _ { \mathrm { r e f } } = \boldsymbol { Z } _ { 0 } ;$ otherwise, the pseudo-waves are linear combinations of the forward and backward waves. For example, suppose that we have an infinite waveguide with all sources in $z > 0 .$ For $z < 0 ,$ we know that ${ a _ { 0 } } = 0 ;$ no wave is incident from this side. However, unless $\scriptstyle { Z _ { \mathrm { r e f } } = Z _ { 0 } } ,$ we will find that a and b are both nonzero in this case.

Another contrast is that, as a function of $z , a _ { 0 }$ and $b _ { 0 }$ have a simple exponential dependence while a and b are complicated functions of z due to interference between the forward and backward traveling waves. For illustration, Fig. 4 plots the magnitudes of ${ \pmb a } _ { 0 }$ and ${ \pmb b _ { 0 } }$ for a line which is uniform in $z < 0$ but has an obstacle of reflection coefficient $T = 0 . 2$ located at ${ \pmb z } = { \pmb 0 }$ . In contrast, Fig. 5 plots the magnitudes of the associated pseudo-waves a and b with $Z _ { \mathrm { r e f } }$ chosen to make b vanish at $z = 0 ,$ Figure 5 demonstrates not only the complicated behavior of a and b with respect to z but also the fact that the change of reference impedance forces b to vanish at only a single point. It is clearly unrealistic to interpret a and b as incident" and “reflected" waves.

In contrast to ${ \pmb a } _ { \mathbf { 0 } }$ and ${ \pmb b _ { 0 } } ,$ a and b generally depend on the normalization which determines lvol, lil, and $\scriptstyle | Z _ { 0 } |$ . This dependence helps to explain a potential paradox. Assume, for instance, that $Z _ { 0 } = 5 0 \ \Omega$ . If $\bar { Z } _ { \mathrm { r e f } } = 5 0 \Omega ,$ , then the pseudo-waves are equal to the traveling waves. Now, since lZdl is arbitrary, depending on how we define ${ \mathfrak { u } } _ { 0 } ,$ we can easily refine $\scriptstyle z _ { 0 }$ to, say, 100 Ω. Are not the pseudo-waves still equal to the traveling waves, even though $\begin{array} { r } { Z _ { \mathrm { r e f } } \neq Z _ { 0 } ? } \end{array}$ In fact, they are not, for the change in $^ { \mathfrak { u } _ { \mathfrak { d } } }$ leads to a renormalization of v and i [see Eqs. (12) and (13)] and therefore a renormalization of a and b through Eqs. (53) and (54). Thus, the pseudo-waves are no longer equal to the traveling waves unless we shift $Z _ { \mathrm { r e f } }$ to 100 Ω as well. This normalization dependence of the pseudo-waves, in contrast to the traveling waves, further illustrates the fact that they are not physical waves but instead only mathematical artifacts.

![](images/126dff0b8208cae07ae5181d529f04b9b3bf3df45be8a9e548c45304b88700b8.jpg)  
Fig. 4. The magnitudes of the incident (ao) and rcflectcd $( b _ { 0 } )$ traveling waves near a termination at ${ \pmb z } = { \bf 0 }$ with reflection coefficient $I _ { 0 } = 0 . 2 .$ The propagation constant is $0 . 0 0 5 + 0 . 1 j$ . The waves depend exponentially on z.

![](images/8727d03744fc540c0ca99d0d6b659243cdda3e402716988fbf38a6931a882ac6.jpg)  
Fig. 5. The magnitudes of the pseudo-waves a and b for the example of Fig. 4. The reference impedance $Z _ { \mathrm { r e f } }$ is chosen so as to make the pseudo-reflection coefficient $\scriptstyle { \Gamma ( Z _ { \mathrm { r e f } } ) }$ vanish at the termination reference plane. Since the waves depend in a complicated fashion on $z , \dot { T } ( Z _ { \mathrm { r e f } } )$ vanishes only at $z = 0$

Finally, the condition $\mathbb { R } \mathrm { e } ( Z _ { \mathrm { r e f } } ) \geqslant 0$ that we have imposed on the reference impedance corresponds to the condition $\mathtt { R e } ( Z _ { 0 } ) \geqslant 0$ that we imposed earlier on the characteristic impedance. Therefore, it is always possible to choose $\begin{array} { r } { Z _ { \mathrm { r e f } } = Z _ { 0 } . } \end{array}$

Since the most convenient choice of ${ \pmb Z } _ { \mathrm { r e f } }$ depends on the application, it will prove useful to construct a procedure to transform the pseudo-waves in accordance with a change of reference impedance. This is considered below.

## 3.3 Voltage Standing Wave Ratio

To illustrate the distinction between the traveling waves and the pseudo-waves, we introduce the voltage standing wave ratio (VSWR). For simplicity, we limit discussion to the lossless case ${ \pmb a } = { \bf 0 } ,$ in which case the fields in the waveguide are strictly periodic in z with period $2 \pi / \beta$ . The VSWR is defined to be the ratio of the maximum to the minimum electric field magnitude, which reduces to

$$
\begin{array} { r } { \mathrm { V S W R } \equiv \frac { \underset { z } { \operatorname* { m a x } } | { E } _ { t } ( z ) | } { \underset { z } { \operatorname* { m i n } } | { E } _ { t } ( z ) | } = \frac { \underset { z } { \operatorname* { m a x } } | { \nu } ( z ) | } { \underset { z } { \operatorname* { m i n } } | { \nu } ( z ) | } } \end{array}
$$

$$
= \frac { \left| a _ { 0 } \right| + \left| b _ { 0 } \right| } { \left| a _ { 0 } \right| - \left| b _ { 0 } \right| } { = } \frac { 1 + \left| \varGamma _ { 0 } \right| } { 1 - \left| \varGamma _ { 0 } \right| } .\tag{60}
$$

In the lossless case, the magnitudes of $a _ { 0 } , b _ { 0 } ,$ and $T _ { 0 }$ are independent of z.

Equation (60) illustrates that the VSWR, a quantity which is determined solely from the electric fields, is directly related to the ratio of traveling waves. In fact, it is the interference between these traveling waves that produces the periodicity. The pseudo-waves cannot be measured by such a procedure because they have no physical manifestation.

The pseudo-waves reduce to the traveling waves when the reference impedance is equal to the characteristic impedance. Therefore, the reference impedance of the reflection coefficient derived from a VSWR measurement is equal to $\scriptstyle z _ { 0 } .$ This provides another argument that $Z _ { 0 }$ is the natural choice of reference impedance.

## 3.4 Scattering and Pseudo-Scattering Matrices

Consider a linear waveguide circuit which connects an arbitrary number of (generally) nonidentical, uniform semi-infinite waveguides which are uncoupled away from the junction. In each waveguide, a cross-sectional reference plane is chosen at which only a single mode exists. If the mode of interest is dominant, this can be ensured by choosing the reference plane sufficiently far from the junction that higher-order modes have decayed to insignificance.

For each waveguide port i, we choose a reference impedance $\bar { Z } _ { \tau e t , } ^ { i }$ in terms of which the pseudowave amplitudes $a _ { i } ( Z _ { \mathrm { r e f } } ^ { i } )$ and $\pmb { b } _ { i } ( Z _ { \mathrm { r e f } } ^ { i } )$ at port i are defined by Eqs. (53) and (54). The orientation is such that the "forward" direction is toward the junction. We define column vectors a and b whose elements are the ${ \pmb a } _ { i }$ and $b _ { i } .$ The vector of outgoing pseudo-waves b is linearly related to the vector of incoming pseudo-waves a by the pseudo-scattering matrix S:

$$
b = 5 a .\tag{61}
$$

Although S depends on the choice of reference impedance at each port, we have suppressed notation which would explicitly acknowledge that fact.

We likewise define the vectors of incoming and outgoing traveling wave intensities ${ \tt a } _ { 0 }$ and ${ \sf b } _ { 0 }$ whose elements are the ao and bo. These two vectors are related by the (true) scattering matrix ${ \mathsf { S } } ^ { 0 }$

$$
{ \sf b } _ { 0 } = { \sf S } ^ { 0 } { \sf a } _ { 0 } .\tag{62}
$$

If $\mathbf { \mathcal { Z } ^ { i } } _ { \mathrm { r e f } } = \mathbf { \mathcal { Z } ^ { i } } _ { 0 }$ for each port i, then $\mathsf { S } = \mathsf { S } ^ { 0 } .$ In other words, the pseudo-scattering matrix is equal to the scattering matrix when the reference impedance at each port is equal to the respective characteristic impedance.

The reflection coefficient $T _ { 0 }$ is the single element of the scattering matrix S of a one-port. The same is also true of $\bar { r }$ and S.

We can say more about S in special cases. For example, the net power into a passive circuit is nonnegative. From (57), this requires that

$$
\mathrm { R e } ( \mathrm { a } ^ { \dag } [ 1 - \mathbb { S } ^ { \dag } \mathbb { S } + 2 j \vee \mathbb { S } ] \mathrm { a } ) \geq 0 .\tag{63}
$$

where $" ( " \dagger ^ { , } ) "$ indicates the Hermitian adjoint (conjugate transpose) and V is a diagonal matrix with elements equal to Im $( Z _ { \mathrm { r e f } } ^ { i } ) / { \mathrm { R e } } ( \bar { Z } _ { \mathrm { r e f } } ^ { i } )$ . If the circuit is lossless, the inequality in Eq. (63) can be replaced by an equality. If all of the reference impedances are real, then Eq. (63) implies that $1 - 5 ^ { \dagger } S$ is positive semi-definite. If, in addition, the circuit is lossless, then ${ \mathsf { S } } ^ { \dagger } { \mathsf { S } } = { \mathsf { I } } ;$ that is, S is unitary.

Another useful property of S is a result of electromagnetic reciprocity and is therefore demonstrable when all the materials comprising the junction have symmetric permittivity and permeability tensors; in using Eqs. (2)-(7), we have already assumed as much in the waveguides themselves. As shown in Appendix D and also in Ref. [14], the reciprocity condition is

$$
\frac { S _ { j i } } { S _ { i j } } = \frac { K _ { i } } { K _ { j } } \ : \frac { 1 - j \ : \mathrm { I m } ( Z _ { \mathrm { r e f } } ^ { i } ) / \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { i } ) } { 1 - j \ : \mathrm { I m } ( Z _ { \mathrm { r e f } } ^ { j } ) / \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { j } ) } ,\tag{64}
$$

where the reciprocity factor $\pmb { K } _ { i }$ is given by

$$
K _ { i } \equiv \frac { \widetilde { p } _ { 0 i } } { p _ { 0 i } * } .\tag{65}
$$

Here

$$
\widetilde { \boldsymbol { p } } _ { 0 } \equiv \int _ { S } \boldsymbol { e } _ { t } \times \boldsymbol { h } _ { t } \cdot \boldsymbol { z } \ \mathrm { d } S\tag{66}
$$

and the additional subscript i refers to the port. When $\boldsymbol { Z } _ { \mathrm { r e f } } = \boldsymbol { Z } _ { 0 }$ at each port, Eq. (64) simplifies to

$$
\frac { S _ { j i } ^ { 0 } } { S _ { i j } ^ { 0 } } = \frac { \widetilde { p } _ { 0 i } } { \mathbf { R e } ( p _ { 0 i } ) } \frac { \mathbf { R e } ( p _ { 0 j } ) } { \widetilde { p } _ { 0 j } } .\tag{67}
$$

The significance of Eq. (64) is that, in contrast to conventional expectations, electromagnetic reciprocity does not necessarily lead to symmetry of the S matrix. In lossless waveguides, $\dot { K _ { i } } = 1$ and $\scriptstyle z _ { 0 }$ is real, so $\mathtt { S } ^ { 0 }$ is symmetric and we need only choose each reference impedance equal to the corresponding characteristic impedance to ensure a symmetric S. In lossy waveguides, $K _ { i }$ is not generally equal to 1. Although $K _ { i } \approx 1$ for typical waveguides, calculations show that it may be much less than 1 in certain guides with very lossy dielectrics [14]. Furthermore, it is not always desirable or even possible to choose a real reference impedance, and a complex reference impedance generally destroys the symmetry of S even when $\bar { K } _ { i } = 1$ . For devices with more than two ports, it is not generally possible to choose the reference impedances so as to make S symmetric. S can always be made symmetric for a two-port, but the phase of the appropriate $Z _ { \mathrm { r e f } }$ at each port depends on $K _ { i }$ at both ports.

Experiments which illustrate the effect of the phase of the reference impedance on the symmetry of S are reported in Refs. [14] and [15].

## 3.5 The Cascade Matrix

Equation (61) denotes a linear relation between the a and $b _ { i } ,$ If the circuit of interest is a two-port with $\pmb { S } _ { 2 1 } \neq 0 ,$ we can express the same relationship using the cascade matrix R, which relates the various pseudo-waves by

$$
\left[ b _ { 1 } ( Z _ { \mathrm { r e f } } ^ { i } ) \right] \ = \ \mathsf { R } ^ { i j } \Big [ \mathsf { \pmb { a } } _ { 2 } ( Z _ { \mathrm { r e f } } ^ { j } ) \Big ] \ ,\tag{68}
$$

The indices in the superscript of $\mathsf { R } ^ { i j }$ indicate that the reference impedance at port 1 is $Z _ { \mathrm { r e f } } ^ { i }$ and that at port 2 is $Z _ { \mathrm { r e f } } ^ { j } .$

Formulas for the conversion between scattering and cascade matrices are readily available [4,16]. For completeness, we repeat them here:

$$
\mathsf { R } { = } \frac { 1 } { S _ { 2 1 } } \left[ \begin{array} { c c } { S _ { 1 2 } S _ { 2 1 } { - } S _ { 1 1 } S _ { 2 2 } \quad } & { S _ { 1 1 } } \\ { - S _ { 2 2 } \quad } & { 1 } \end{array} \right]\tag{69}
$$

and

$$
\mathbb { S } = \frac { 1 } { R _ { 2 2 } } \left[ { R _ { 1 2 } \atop 1 } { R _ { 1 1 } R _ { 2 2 } } - R _ { 1 2 } R _ { 2 1 } \atop - R _ { 2 1 } \right] .\tag{70}
$$

The cascade matrix of two series-connected twoports is the product of the two cascade matrices as long as the connecting ports are composed of identical waveguides, with identical reference impedances, joined without discontinuity. Since this holds true regardless of the reference impedances, the introduction of terminology such as “pseudocascade matrix" would be needlessly confusing. We will, however, introduce the special notation $A ^ { 0 }$ to describe the cascade matrix which satisfies

$$
{ \bf \Big [ } { b _ { 0 1 } } { \Big ] } = { \sf R } ^ { 0 } { \Big [ } _ { b _ { 0 2 } } ^ { a _ { 0 2 } } { \Big ] } .\tag{71}
$$

R is equal to $R ^ { 0 }$ when $\scriptstyle { Z _ { \mathrm { r e f } } ^ { i } = Z _ { 0 } ^ { i } }$ for each port i.

## 3.6 The Impedance Matrix

The impedance matrix Z relates the column vectors V and i, whose elements are the waveguide voltages and currents at the various ports:

$$
\mathsf { \pmb { v } } = \mathsf { \pmb { Z } } \mathsf { \pmb { l } } .\tag{72}
$$

In contrast to S and R, Z is independent of the reference impedance since v and i are also. This makes Z particularly interesting for metrological purposes. Z does, however, depend on the normalization of $v _ { 0 } .$

The relation between S and Z is explored in Appendix E. The results are

$$
\begin{array} { r l } & { \mathbb { S } = \bigcup ( \mathbb { Z } - \mathbb { Z } _ { t 0 i } ) ( \mathbb { Z } + \mathbb { Z } _ { t 0 i } ) ^ { - 1 } \bigcup ^ { - 1 } = } \\ & { } \\ & { \bigcup ( \mathbb { Z } Z _ { t 0 i } ^ { - 1 } - 1 ) ( \mathbb { Z } Z _ { r 0 i } ^ { - 1 } + 1 ) ^ { - 1 } \bigcup ^ { - 1 } } \end{array}\tag{73}
$$

and inversely

$$
\begin{array} { r } { \mathsf { Z } = ( \mathsf { I } - \mathsf { U } ^ { - 1 } \mathsf { S } \mathsf { U } ) ^ { - 1 } ( \mathsf { I } + \mathsf { U } ^ { - 1 } \mathsf { S } \mathsf { U } ) \mathsf { Z } _ { \mathsf { r e f } } . } \end{array}\tag{74}
$$

Here $z _ { e f }$ is a diagonal matrix whose elements are the $Z _ { r e t } ^ { i }$ and U is another diagonal matrix defined by

$$
\mathsf { U } \equiv \mathrm { d i a g } \Bigl ( \frac { | \boldsymbol { v } _ { \mathrm { 0 i } } | } { \boldsymbol { u } _ { \mathrm { i s } } } \frac { \sqrt { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { i } ) } } { | Z _ { \mathrm { r e f } } ^ { i } | } \Bigr ) .\tag{75}
$$

The factor U, which does not appear in other expressions relating S with Z [3,4], generalizes the earlier results to problems including complex fields and reference impedances.

Appendix D demonstrates that the off-diagonal elements of Z are related by

$$
\frac { \mathcal { Z } _ { j i } } { \mathcal { Z } _ { i j } } = \frac { K _ { i } } { K _ { j } } \frac { { \nu _ { 0 } } _ { i } ^ { * } } { \nu _ { 0 } } \frac { \nu _ { 0 j } } { { \nu _ { 0 j } } ^ { * } } .\tag{76}
$$

Thus $z ,$ like S, is generally asymmetric, even when the circuit is reciprocal and u is chosen real at each port. The asymmetry of Z is not a result of wave normalization, for $z$ is defined without reference to waves.

The admittance matrix Y is the inverse of Z and satisfies

$$
\mathbf { i } = \mathbf { Z } ^ { - 1 } \mathbf { v } = \mathsf { Y } \mathbf { v } .\tag{77}
$$

## 3.7 Change of Reference Impedance

As discussed earlier, the most convenient choice of reference impedance depends on the circumstances. In order to accómmodate the various choices, we consider the relationship between the pseudo-wave amplitudes based on different reference impedances. By expressing a (Zet) and b(Zef) in terms of v and i using Eqs. (53) and (54) and v and i in terms of a (Zī) and b (Z) using Eqs. (55) and (56), we arrive at the linear relationship

$$
\begin{array} { r } { \left[ a \left( Z _ { \mathrm { r e f } } ^ { n } \right) \right] = { \mathbb { Q } } ^ { m n } \Big [ _ { b \left( Z _ { \mathrm { r e f } } ^ { n } \right) } ^ { a \left( Z _ { \mathrm { r e f } } ^ { n } \right) } \Big ] , } \end{array}\tag{78}
$$

where

$$
\mathsf { Q } ^ { n m } \equiv \frac { 1 } { 2 Z _ { \mathrm { r e f } } ^ { m } } \left| \frac { Z _ { \mathrm { r e f } } ^ { m } } { Z _ { \mathrm { r e f } } ^ { n } } \right| \sqrt { \frac { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { n } ) } { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { m } ) } } \mathrm { ~ . ~ }
$$

$$
\begin{array} { r l } { \left[ Z _ { \mathrm { r e f } } ^ { m } + Z _ { \mathrm { r e f } } ^ { n } } & { { } Z _ { \mathrm { r e f } } ^ { m } - Z _ { \mathrm { r e f } } ^ { n } \right] } \\ { \left[ Z _ { \mathrm { r e f } } ^ { m } - Z _ { \mathrm { r e f } } ^ { n } \right. } & { { } \left. Z _ { \mathrm { r e f } } ^ { m } + Z _ { \mathrm { r e f } } ^ { n } \right] } \end{array} .\tag{79}
$$

This can be put into more conventional form by defining a quantity $N _ { n m }$ , analogous to the "turns ratio" of a conventional transformer, by

$$
N _ { n m } \equiv \sqrt { \frac { Z _ { \mathrm { r e f } } ^ { n } } { Z _ { \mathrm { r e f } } ^ { m } } } ,\tag{80}
$$

so Eq. (78) becomes

$$
{ \sf Q } ^ { n m } \equiv \frac { 1 } { 2 | N _ { n m } | ^ { 2 } } \sqrt { \frac { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { n } ) } { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { m } ) } } \left[ 1 + N _ { n m } ^ { 2 } \ 1 - N _ { n m } ^ { 2 } \right] .\tag{81}
$$

Equation (81) is similar to the two-port cascade matrix of a classical impedance transformer [4], in which the square root in Eq. (81) is replaced by $N _ { n m } ^ { * }$ . When $\bar { Z } _ { \mathrm { r e f } } ^ { m }$ and $Z _ { \mathrm { r e f } } ^ { n }$ are both real, the two matrices are identical. However, Eq. (81) can be determined neither from the classical result nor from any other lossless analysis. This explains why the result $\mathbf { E q } .$ (79) does not, to our knowledge, appear in previous literature. Equations (78) and (79) are an exact expression of the complex impedance transform. We may accurately refer to the pseudowaves as impedance-transformed traveling waves.

Two consecutive transforms can be represented as a single transform from the initial to the final reference impedance by

$$
{ \mathsf { Q } } ^ { n m } { \mathsf { Q } } ^ { m p } = { \mathsf { Q } } ^ { n p } .\tag{82}
$$

Also,

$$
\mathsf { Q } ^ { n } = \mathsf { I } ,\tag{83}
$$

where I is the identity matrix. As a result,

$$
[ { \mathsf { G } } ^ { m m } ] ^ { - 1 } = { \mathsf { G } } ^ { m n } ,\tag{84}
$$

which states that the transformation is inverted by a return to the original reference impedance.

The determinant of ${ \mathsf Q } ^ { n m }$

$$
\operatorname* { d e t } [ \boldsymbol { \Omega } ^ { n m } ] = \left[ 1 - j \frac { \mathrm { I m } ( Z _ { \mathrm { r e f } } ^ { m } ) } { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { m } ) } \right] \left[ 1 - j \frac { \mathrm { I m } ( Z _ { \mathrm { r e f } } ^ { n } ) } { \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { n } ) } \right] ^ { - 1 } .\tag{85}
$$

The scattering matrix associated with $\mathbf { Q } ^ { n m }$ is symmetric if and only if det $[ \mathsf { Q } ^ { m } ] = 1$ , which is true if and only if the phases of $Z _ { \mathrm { r e f } } ^ { m }$ and $Z _ { \mathrm { r e f } } ^ { n }$ are identical. Equation (85) demonstrates that the scattering matrix representing the transform between a complex and a real impedance is in general asymmetric. In other words, a symmetric scattering matrix cannot remain symmetric when the reference impedance at a single port changes from a real to a nonreal value. This result is closely related to Eq. (64) since, from Eq. (69), the determinant of a cascade matrix is equal to $\pmb { S } _ { 1 2 } / \pmb { S } _ { 2 1 }$ of the associated scattering matrix $\dot { \mathsf { \pmb { \mathsf { S } } } } .$

$\mathbf { Q } ^ { n m }$ can be expressed in yet another form:

$$
{ \tt Q } ^ { n m } = \sqrt { \frac { 1 - j \mathrm { \Delta I m } ( Z _ { \mathrm { r e f } } ^ { m } ) / \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { m } ) } { 1 - j \mathrm { \Delta I m } ( Z _ { \mathrm { r e f } } ^ { n } ) / \mathrm { R e } ( Z _ { \mathrm { r e f } } ^ { n } ) } } .
$$

$$
\frac { 1 } { \sqrt { 1 -  { \mathit { \Gamma } } _ { m m } ^ { 2 } } } \left[ \begin{array} { l l } { 1 } & {  { \mathit { \Gamma } } _ { n m } } \\ {  { \mathit { \Gamma } } _ { n m } } & { 1 } \end{array} \right] ,\tag{86}
$$

where we use the definition

$$
\Gamma _ { n m } \equiv \frac { Z _ { \mathrm { r e f } } ^ { m } - Z _ { \mathrm { r e f } } ^ { n } } { Z _ { \mathrm { r e f } } ^ { m } + Z _ { \mathrm { r e f } } ^ { n } } .\tag{87}
$$

This form is convenient in the computation of the effect of the complex impedance transform on the reflection coefficient. The reflection coefficient is transformed by

$$
T ( Z _ { \mathrm { r e f } } ^ { n } ) = \frac { { \varGamma } _ { n m } + T ( Z _ { \mathrm { r e f } } ^ { m } ) } { 1 + { \varGamma } _ { n m } T ( Z _ { \mathrm { r e f } } ^ { m } ) } .\tag{88}
$$

A short circuit, defined as a perfectly conducting electric wall spanning the entire cross section of the waveguide, forces the tangential electric field to vanish at the reference plane. A short therefore requires ${ \pmb \nu } = { \bf 0 }$ and $b = - a$ . As a result, the reflection coefficient is ${ \cal T } _ { 0 } = - 1$ . We can see from Eq. (88) that the transform of a perfect short remains $\dot { T } ( Z _ { \mathrm { r e f } } ^ { n } ) = - 1$ independent of the reference impedance. The only other reflection coefficient which is independent of the reference impedance is the perfect open circuit (magnetic wall), at which the transverse magnetic field vanishes so that $i = 0 ,$ $\pmb { b } = \pmb { a }$ , and $\boldsymbol { r } = + 1$ . The unique status of the short and open is related to their unique physical manifestations.

If $T ( Z _ { \mathrm { r e f } } ^ { m } ) { = } 0$ (perfect match) then $T ( Z _ { \mathrm { r e f } } ^ { n } ) = { \cal T } _ { n m }$ Conversely, if $T ( Z _ { \mathrm { r e f } } ^ { m } ) = - \ : { \Gamma _ { n m } }$ then $T ( Z _ { \mathrm { r e f } } ^ { n } ) { = } \mathrm { 0 }$

## 3.8 Multiport Reference Impedance Transformations

A direct, if somewhat complicated, means of computing the transformation of S due to a change of reference impedance begins by computing Z using Eq. (74). Subsequently, Eq. (73) is used with the new reference impedance to calculate the transformed S. This procedure works because Z is independent of reference impedance.

If the circuit under consideration is a two-port, the simplest way of computing the transform is to compute the associated cascade matrix $\mathsf { R } ,$ perform the transform on $\mathsf { R } ,$ and convert back to an S matrix. To determine the effect of the transform on $\mathsf { R } ,$ we insert Eq. (78) into the right hand side of Eq. (68). In order to do the same with the left hand side, we need use the result that, due to symmetry of ${ \pmb { \mathbb { Q } } } ^ { n m }$ about both diagonals, Eq. (78) implies that

$$
[ b ( Z _ { \mathrm { r e f } } ^ { n } ) ] = { \sf G } ^ { n q } { [ b ( Z _ { \mathrm { r e f } } ^ { q } ) ] } ) .\tag{89}
$$

Upon making these replacements and using Eq. (84), we can put Eq. (68) into a form relating $b _ { 1 } ( Z _ { \mathrm { r e f } } ^ { p } )$ and $a _ { 1 } ( Z _ { \mathrm { r e f } } ^ { p } )$ to $\pmb { b _ { 2 } } ( Z _ { \mathrm { r e f } } ^ { q } )$ and $a _ { 2 } ( Z _ { \mathrm { r e f } } ^ { q } )$ . The result is that

$$
{ \mathsf { R } } ^ { p q } = { \mathsf { Q } } ^ { p m } { \mathsf { R } } ^ { m n } { \mathsf { Q } } ^ { n q } .\tag{90}
$$

This equation displays the effect on the cascade matrix of altering the reference impedance of port 1 from $Z _ { \mathrm { r e f } } ^ { m }$ to $Z _ { \mathrm { r e f } } ^ { p }$ and that of port 2 from $Z _ { \mathrm { r e f } } ^ { n }$ to $Z q _ { e t }$ This is a concise expression of the complex impedance transform.

īn the special but common case in which the two ports use identical reference impedances, Eq. (90) simplifies. In transforming the reference impedance of both ports from $Z _ { \mathrm { r e f } } ^ { m }$ to $Z _ { \mathrm { r e f } } ^ { p } ,$ the cascade matrix is transformed by

$$
\mathsf { R } ^ { p p } = \mathsf { Q } ^ { p m } \mathsf { R } ^ { m m } \mathsf { Q } ^ { m p } =
$$

$$
\frac { 1 } { 1 - { \cal T } _ { p m } ^ { 2 } } \left[ \begin{array} { c c } { { 1 } } & { { { \cal T } _ { p m } } } \\ { { { \cal T } _ { p m } } } & { { 1 } } \end{array} \right] { \sf R } ^ { m m } \bigg [ - \frac { 1 } { { \cal T } _ { p m } } \begin{array} { c c } { { - { \cal T } _ { p m } } } \\ { { 1 } } \end{array} \bigg ] \ .\tag{91}
$$

This transformation was used in Ref. [16].

## 3.9 Load Impedance

The load impedance is defined as the single element of the impedance matrix describing a linear one-port. At the reference plane, at which only a single mode exists, the load impedance is defined in terms of v and i as

$$
Z _ { \mathrm { l o a d } } \equiv \frac { \upsilon } { i } .\tag{92}
$$

From Eq. (19), the power absorbed by the load can be expressed as

$$
P = \lvert i \rvert ^ { 2 } R _ { \mathrm { l o a d } } = \lvert \upsilon \rvert ^ { 2 } \frac { R _ { \mathrm { l o a d } } } { \lvert Z _ { \mathrm { l o a d } } \rvert ^ { 2 } } ,\tag{93}
$$

where $R _ { \mathrm { l o a d } } \equiv \mathrm { R e } ( Z _ { \mathrm { i o a d } } )$ . Power conservation ensures that, for a passive one-port, $R _ { \mathrm { l o a d } } \gtrsim 0$ For the remainder of this section, we assume that the load of interest is passive in order to avoid conflict with the requirement that $\mathbb { R } e ( Z _ { \mathrm { r e f } } ) \geqslant 0$

The load impedance, like v and $i ,$ is independent of the reference impedance. Unlike the result of low-frequency circuit theory, however, $\mathbf { \tilde { \Pi } } _ { Z _ { \mathrm { l o a d } } }$ is not a unique property of the one-port itself but instead depends on the fields of the mode incident upon it. Illumination of the same device by a different waveguide, or even a different mode of the same waveguide, may result in a drastically different $Z _ { { \mathrm { l o a d } } }$ $\mathbf { \tilde { \Pi } } _ { Z _ { \mathrm { l o a d } } }$ also depends on the normalization which determines u and $i _ { 0 } ,$ for this affects v and i.

Using Eq. (92) in Eq. (54), we see that, when the reference impedance is equal to the load impedance, we have $b ( Z _ { \mathrm { l o a d } } ) = 0$ . From Eq. (58), this implies that

$$
\begin{array} { r } { T ( Z _ { \mathrm { l o a d } } ) { = } 0 . } \end{array}\tag{94}
$$

In other words, when $Z _ { \mathrm { r e f } } = Z _ { \mathrm { l o a d } } ,$ the reflection coefficient vanishes. In this reference impedance, the load looks like a perfect match. Likewise, if we insist that the reflection coefficient vanishes when a certain load is connected to our line, we have effectively chosen the reference impedance to be equal to $\dot { Z } _ { \mathrm { l o a d } } .$ This is relevant to the calibration problem considered below. Keep in mind, however, that it may be difficult to establish a value for $\mathbf { \tilde { \mu } } _ { Z _ { \mathrm { l o a d } } }$ since that depends on the waveguide as well as the load.

Using Eq. (94) along with Eqs. (87) and (88), we find that

$$
\Gamma ( Z _ { \mathrm { r e f } } ) = \frac { Z _ { \mathrm { l o a d } } - Z _ { \mathrm { r e f } } } { Z _ { \mathrm { l o a d } } + Z _ { \mathrm { r e f } } } .\tag{95}
$$

We can also solve for $Z _ { \mathrm { l o a d } } \mathrm { : }$

$$
Z _ { \mathrm { l o a d } } { = } Z _ { \mathrm { r e f } } \ \frac { 1 + \varGamma ( Z _ { \mathrm { r e f } } ) } { 1 - \varGamma ( Z _ { \mathrm { r e f } } ) } .\tag{96}
$$

This produces the same result regardless of the reference impedance with respect to which I is defined. If we choose $Z _ { \mathrm { r e f } }$ equal to the characteristic impedance $\mathcal { Z } _ { 0 } ,$ these two equations are identical to those of ordinary waveguide circuit theory and to the theory of Ref. [6].

We see from Eq. (96) that the load impedance of a short is 0 and that of an open is ∞.

As an example of a load, consider the use of a semi-infinite transmission line with characteristic impedance $\mathbf { { Z } _ { 1 } }$ to terminate a transmission line with characteristic impedance $Z _ { 0 } .$ In general, the reflection coefficient and the load impedance are impossible to compute. One common approximation,

based on the notions of low-frequency circuit theory, is that both v and i are continuous at the interface. This assumption leads to the result that the load impedance of the line is simply its characteristic impedance. This allows the reflection coefficient to be determined by Eq. (95).

Unfortunately, the assumption leading to this result is not generally valid, since v and i are not generally continuous at an interface. Recall that v and i are not strictly related to true voltage or current. The actual boundary conditions at the interface require continuity of tangential fields, and these cannot in general be satisfied without the presence of an infinity of higher order modes at the discontinuity. By contrast, the waveguide voltage and current are indicative of the intensities of only a single mode. The reflection coefficient cannot therefore be determined from waveguide circuit parameters. For an explicit example, consider the case in which ${ \cal Z } _ { 0 } = { \cal Z } _ { 1 }$ while the two transmission lines are physically dissimilar. In this case, the assumption that the load impedance equals ${ \cal Z } _ { 1 }$ leads to the result that there is no reflection of traveling waves. In fact, reflection must take place due to the discontinuity at the interface. Exceptions occur only when no higher-order modes are generated. An example is coaxial lines of lossless conductors which differ only in the dielectric material. In this peculiar example, the reflection coefficient can be computed exactly from $\mathbf { \mathcal { Z } } _ { 0 }$ and $Z _ { 1 } .$ In other examples, the result is at best approximate.

## 4. Waveguide Metrology

In this section, we apply the theoretical results of the previous sections to the elucidation of the basic problems of waveguide metrology, which aims to characterize waveguide circuits in terms of appropriate matrix descriptions.

## 4.1 Measurability and the Choice of Reference Impedance

In addition to the slotted line, which measures VSWR directly, the primary instrument used to characterize waveguide circuits is the vector network analyzer (VNA). Here we restrict ourselves to a two-port VNA, which provides a measurement $\pmb { M _ { i } }$ of the product

$$
{ \boldsymbol { \mathsf { M } } } _ { i } = { \boldsymbol { \mathsf { X } } } { \boldsymbol { \mathsf { T } } } _ { i } { \overline { { \mathsf { Y } } } } .\tag{97}
$$

Here $\daleth _ { i }$ is the cascade matrix of the device i under test, X and $\boldsymbol { \mathsf { Y } }$ are constant, non-singular matrices which describe the instrument, and

$$
\overline { { \mathsf { Y } } } \equiv \left[ { \begin{array} { l } { 0 \ 1 } \\ { 1 \ 0 } \end{array} } \right] \mathsf { Y } ^ { - 1 } \left[ { \begin{array} { l } { 0 \ 1 } \\ { 1 \ 0 } \end{array} } \right]\tag{98}
$$

is the reverse cascade matrix corresponding to Y. The problem of network analyzer calibration is to determine X and Y by the insertion and measurement of known devices i. With X and Y known, Eq. (97) determines $T _ { i }$ from the measured $M _ { i }$

X, Y, and $\daleth _ { i }$ are commonly considered unique, and a calibration process which determines them uniquely is applied. However, as we have seen in this paper, the cascade matrix T depends on the reference impedances with which it is defined. Thus, any number of calibrations lead to legitimate measurements of a cascade matrix and therefore legitimate measurements of pseudo-scattering parameters, although with varying port reference impedances. We refer to these calibrations, each of which is related to any other by an impedance transform, as consistent. Any calibration which is not related to a consistent calibration by an impedance transform will not yield measurements of pseudo-scattering parameters. Such a calibration is inconsistent. For example, X and Y may be determined in such a way that the resulting measurement of an open circuit is not equal to 1. Such a result is prohibited for pseudo-scattering parameters, so the calibration is inconsistent. It is meaningless to speak of the reference impedance of such a calibration.

The reference impedances of a consistently calibrated VNA are uniquely determined by the calibration. Only when the reference impedance is equal to the characteristic impedance of the line are the resulting pseudo-scattering parameters equal to the actual scattering parameters. Of course, transformation to an alternative reference impedance is possible, but only if the initial reference impedance is known. This section analyzes some common calibration methods to determine their reference impedance.

We assume that the waveguides at the two reference planes and the two corresponding basis functions $\pmb { e _ { t } }$ are identical. When $\scriptstyle { \mathcal { Z } } _ { \mathrm { r e f } }$ at both ports is equal to the characteristic impedance $\scriptstyle z _ { 0 } ,$ we can express Eq. (97) as

$$
M _ { i } = X ^ { 0 } \bar { \mathsf { T } } _ { i } ^ { 0 } \overline { { \mathsf { Y } } } ^ { 0 } .\tag{99}
$$

The single superscript on the network analyzer matrices refers to the reference impedance at the test ports. We do not need to define or discuss a reference impedance at the “measurement ports."

From Eq. (84), the identity matrix can be expressed as $1 = 0 ^ { \circ \cdot } \mathsf { Q } ^ { m 0 } .$ Inserting this into Eq. (99) yields

$$
\mathsf { M } _ { i } = ( \mathsf { X } ^ { 0 } \mathsf { Q } ^ { 0 m } ) ( \mathsf { { Q } } ^ { m 0 } \mathsf { T } _ { i } ^ { 0 } \mathsf { \Omega } \mathsf { Q } ^ { 0 n } ) ( \mathsf { { Q } } ^ { n 0 } \overline { { \mathsf { Y } } } ^ { 0 } ) = \mathsf { X } ^ { m } \mathsf { T } _ { i } ^ { m n } \overline { { \mathsf { Y } } } ^ { n } ,\tag{100}
$$

where

$$
\mathsf { X } ^ { m } \equiv \mathsf { X } ^ { 0 } \mathsf { Q } ^ { 0 m } ,\tag{101}
$$

$$
\overline { { \mathsf { Y } } } ^ { n } \equiv \mathsf { Q } ^ { n 0 } \overline { { \mathsf { Y } } } ^ { 0 } ,\tag{102}
$$

and

$$
{ \sf T } _ { i } ^ { m n } \equiv { \sf G } ^ { m 0 } { \sf T } _ { i } ^ { 0 } { \sf Q } ^ { 0 n }\tag{103}
$$

are the impedance-transformed cascade matrices. If the calibration procedure determines that $\pmb { \chi } = \pmb { \chi } ^ { m }$ and $\curlyvee = \forall ^ { n }$ , then subsequent calibrated measurements will determine the matrix T/™". If X" and Y" have the form of Eqs. (101) and (102), the VNA will be consistently calibrated to reference impedances $Z _ { \mathrm { r e f } } ^ { m }$ on port 1 and $Z _ { \mathrm { r e f } } ^ { n }$ on port 2.

The most accurate method of VNA calibration is TRL [17, 18], a moniker which refers to the use of a "thru," and "reflect," and a "line." The "thru" is a length of transmission line which connects at either end to a test port. The line standard is a longer section of transmission line. The “reflect" is a symmetric and transmissionless but otherwise arbitrary two-port embedded in a section of transmission line. The method assumes that each measured device has an identical transition from the test port to the calibration reference plane. The reference planes are set to the center of the thru.

The TRL method, like other calibration methods, determines the matrices $\mathsf { X } ^ { m }$ and $\mathsf { Y } ^ { n } .$ However, as we have seen, these two matrices are nonunique since they depend on the reference impedances. Thus, we need to analyze the algorithm to determine which reference impedances are imposed by the calibration.

Our first standard $( i = 1 )$ , an ideal thru, is a continuous connection between two identical lines. Since the traveling waves are not disturbed, the cascade matrix using a reference impedance of $Z _ { 0 }$ must be the identity matrix l:

$$
T _ { 1 } ^ { 0 } = 1 .\tag{104}
$$

If the calibration is consistent but, instead of $Z _ { 0 } ,$ reference impedances $Z _ { \mathrm { r e f } } ^ { m }$ and $Z _ { \mathrm { r e f } } ^ { n }$ are used, then the thru has the cascade matrix

$$
{ \mathsf { T } } _ { 1 } ^ { m n } = { \mathsf { G } } ^ { m 0 } { \mathsf { l } } { \mathsf { Q } } ^ { 0 n } = { \mathsf { Q } } ^ { m n } .\tag{105}
$$

However, the TRL algorithm is constructed so as to force the calibrated measurement of the thru to equal the identity matrix. That is, it imposes the condition that

$$
{ \cal T } _ { 1 } ^ { m n } { = } { \cal G } ^ { m n } { = } { \cal 1 } ,\tag{106}
$$

which, from (86) and (87), is true if and only if

$$
{ \cal Z } _ { \mathrm { r e f } } ^ { m } { = } { \cal Z } _ { \mathrm { r e f } } ^ { n } .\tag{107}
$$

In other words, the algorithm imposes the condition that the reference impedances on both ports be identical. The thru alone cannot provide any information as the value of that reference impedance.

Another result of the TRL algorithm is that the calibrated measurement of the reflect standard is identical on both ports. This again reveals nothing about the port reference impedances except that they are identical.

The ideal line standard (i =2) is a length of transmission line identical to that of the two test ports and connected to them without discontinuity. As a result, there is no reflection of the traveling waves. This requires the cascade matrix of the line, with a reference impedance of $\scriptstyle { Z _ { 0 } , }$ to be

$$
\begin{array} { r } { \mathbb { T } _ { 2 } ^ { 0 } = \biggl [ { e ^ { - \gamma l } \begin{array} { c c } { 0 } \\ { 0 } & { e ^ { + \gamma l } } \end{array} } \biggr ] , } \end{array}\tag{108}
$$

where $\pmb { \gamma }$ is the propagation constant and l is the line length. Since we require identical reference impedances on both ports, the transformed cascade matrix is

$$
{ \sf T } _ { 2 } ^ { m m } = { \sf G } ^ { m 0 } { \sf T } _ { 2 } ^ { 0 } { \sf Q } ^ { 0 m } =
$$

$$
\frac { e ^ { + \gamma l } } { 1 - \Gamma _ { 0 m } ^ { 2 } } ~ \biggl [ - ( 1 - e ^ { - 2 \gamma l } - \Gamma _ { 0 m } ^ { 2 } ~ ( 1 - e ^ { - 2 \gamma l } ) \Gamma _ { 0 m } \biggr ] ,\tag{109}
$$

where $\Gamma _ { 0 m }$ is defined as in Eq. (87)

The TRL algorithm ensures that the cascade matrix in Eq. (109) is diagonal and therefore that the calibrated measurement of the line will be such that $\mathscr { S } _ { 1 1 } = \mathscr { S } _ { 2 2 } = 0$ The off-diagonal elements of (109) are equal and opposite. Assuming that $e ^ { - 2 \gamma t } { \neq } 1$ , Ty is diagonal if and only if $\Gamma _ { 0 m } = 0 ,$ which implies that $Q ^ { 0 m } = 1$ and

$$
{ \cal Z } _ { \mathrm { r e f } } ^ { m } = { \cal Z } _ { 0 } .\tag{110}
$$

That is, the TRL method using a perfect line and thru results in a consistent calibration with identical reference impedances on each port equal to the characteristic impedance of the line. Recall that the condition $\scriptstyle { Z _ { \mathrm { r e f } } = Z _ { 0 } }$ was the condition under which the pseudo-waves are equal to the actual traveling waves. Thus the TRL method calibrates the VNA so as to measure the unique scattering matrix $\mathsf { S } ^ { 0 }$ which relates the actual traveling waves, not some arbitrary pseudo-scattering matrix S.

In the special case $e ^ { - 2 \gamma l } = 1 ,$ as occurs in a lossless line whose phase delay is an integral multiple of 180°, Tmm is diagonal for any $\Gamma _ { 0 m }$ . Therefore, the reference impedance need not be equal to $Z _ { 0 }$ and is in fact indeterminate. This results in the wellknown problem of ill-conditioning in such a case.

We have seen that the TRL method calibrates to a reference impedance of $Z _ { 0 } .$ What happens if we use the TRL algorithm but not the TRL standards? We consider methods which use the thru and reflect but replace the ideal line by some other passive artifact, which we call the surrogate line. The matrix T2 takes the arbitrary form

$$
\boldsymbol { \mathsf { T } _ { 2 } ^ { 0 } } \equiv \left[ \begin{array} { l } { \boldsymbol { A B } } \\ { \boldsymbol { C D } } \end{array} \right] .\tag{111}
$$

Since the use of the thru forces any consistent calibration to have identical reference impedances on each port, the transformation of T2 is

$$
\begin{array}{c} \begin{array} { r l r } { \mathsf { T } _ { 2 } ^ { m m } = \frac { 1 } { \sqrt { 1 -  { T _ { 0 ^ { \cdot } } } ^ { 2 } } } } & { \left[ \begin{array} { l l } { A + B  { T _ { 0 m } } - C  { T _ { 0 m } } - D  { T _ { 0 m } } ^ { 2 } } & \\ { - A  { T _ { 0 m } } - B  { T _ { 0 m } } ^ { 2 } + C + D  { T _ { 0 m } } } & \end{array} \right. } & \\ & { } & \\ & { \left. + A  { T _ { 0 m } } + B - C  { T _ { 0 m } } ^ { 2 } - D  { T _ { 0 m } } \right.} & { ( 1 1 } \end{array}   & { \left. ( 1 1 \right) } & \end{array}\tag{2}
$$

The algorithm attempts to force $\ T _ { 2 } ^ { m m }$ to be diagonal. With a surrogate in place of the line, this may be impossible if $\bar { \mathsf { T } } _ { 2 } ^ { m m }$ has the form of Eq. (112), for we have two equations to be satisfied but only the single variable $\Gamma _ { 0 m }$ . The sum of those two equations produces the requirement

$$
C = - B ,\tag{113}
$$

which is identical to the condition

$$
\pmb { S } _ { 1 1 } ^ { 0 } = \mathbb { S } _ { 2 2 } ^ { 0 }\tag{114}
$$

on the scattering parameters of the standard.

Unless Eq. (114) is satisfied, the analysis reveals a contradiction. The resolution of this problem lies with the realization that $\mathbf { E q } .$ (112) results from the assumption that the calibration is consistent. However, unless Eq. (114) is satisfied, the calibration is inconsistent and Eq. (112) does not apply. This conclusion is almost obvious, given the fact that both the thru and the surrogate line must appear perfectly matched at each port. In order to meet this condition with a consistent calibration, the thru requires identical reference impedances on each port while the surrogate line demands different reference impedances. Consequently, the calibration is inconsistent and no reference impedance exists.

Clearly, the perfect line meets the symmetry criterion (114). However, so do many other artifacts. Given standards that satisfy (114), a consistent calibration is obtained and the condition of diagonality determines $\Gamma _ { 0 m }$ . When $B = C = 0 ,$ as was the case with the TRL method, then $T _ { 0 m } = 0$ and the reference impedance is $\scriptstyle z _ { 0 } .$ In any other case, $\Gamma _ { 0 m }$ is determined by a quadratic equation whose solution is

$$
T _ { 0 n } = \frac { D - A } { 2 B } \pm \sqrt { \left[ \frac { D - A } { 2 B } \right] ^ { 2 } - 1 } .\tag{115}
$$

The cascade parameters $A , B , C ,$ and D can be replaced by the scattering parameters of the standard:

$$
\frac { D - A } { B } = S _ { 1 1 } ^ { 0 } + \frac { 1 } { S _ { 1 1 } ^ { 0 } } - \frac { S _ { 1 2 } ^ { 0 } S _ { 2 1 } ^ { 0 } } { S _ { 1 1 } ^ { 0 } } .\tag{116}
$$

This formally determines the reference impedance, albeit in a somewhat complicated fashion. In the special case $S _ { 1 2 } ^ { 0 } S _ { 2 1 } ^ { 0 } { = } 0 ,$ the insertion of Eq. (116) into (115) leads to the two solutions ${ \cal T } _ { 0 m } = { \cal S } _ { 1 1 } ^ { 0 }$ and $T _ { 0 m } = \dot { 1 } / S _ { 1 1 } ^ { 0 }$ . An analysis lets us reject the second of these. It is then simple to show that

$$
Z _ { \mathrm { r e f } } ^ { m } = Z _ { \mathrm { l o a d } } .\tag{117}
$$

That is, the reference impedance for the calibration is the load impedance of the device used as a standard. As indicated by Eq. (94), this is the appropriate reference impedance so that the calibrated reflection coefficient vanishes.

Since the standard is assumed passive, then, from Eq. (93), $\begin{array} { r } { \mathbf { R e } ( Z _ { \mathrm { l o a d } } ) \geq 0 . } \end{array}$ Therefore, Eq. (117) presents no conflicts with the requirement that $\bf \bar { R e } ( Z _ { r e f } ) \geq 0$

This sort of calibration is known as TRM or LRM [19], where the $" \mathbf { M } ^ { \prime \prime }$ stands for "match." Clearly, the match need not be perfect. If the match is perfect $( S _ { 1 1 } ^ { 0 } = S _ { 2 2 } ^ { 0 } = 0 )$ , then the calibration is identical to that using TRL and will allow the measurement of relations between traveling waves. If the match is symmetric but imperfect and Si2 ${ \cal S } _ { 2 1 } ^ { 0 } = 0 ,$ the LRM calibration is related to the TRL calibration by an impedance transform of both ports to a reference impedance equal to the load impedance of the match. In this case, the VNA calibrated with LRM measures relations not among the traveling waves but among a particular set of pseudo-waves.

Frequently, the match standard is chosen to be a pair of small resistors in the hope that their load impedance is approximately real and constant. This would lead to a useful calibration in which the pseudo-scattering parameters would be measured with respect to a real, constant reference impedance. Unfortunately, it is difficult in practice to design a real and constant load impedance. Furthermore, that impedance is known only after it has been measured with respect to some other calibration. In addition, the load impedance generally depends on the line with respect to which it is measured.

If $\mathcal { S } _ { 1 1 } ^ { 0 } { = } S _ { 2 2 } ^ { 0 } { \neq } 0$ and $\bar { S } _ { 1 2 } ^ { 0 } S _ { 2 1 } ^ { 0 } { \neq } 0 ,$ as would be the case using a symmetric attenuator, the calibration reference impedance depends on $\mathbb { S } _ { 1 2 } ^ { 0 } \mathbb { S } _ { 2 1 } ^ { 0 }$ as well as $\pmb { S _ { 1 1 } ^ { 0 } }$ of the standard. This is an important point to consider in designing the match standard, for any coupling between the two resistors will induce a shift in the reference impedance compared to the load impedance of either resistor alone.

Another useful example is the mismatched line standard. The TRL method using an ideal, matched line led to a reference impedance equal to the characteristic impedance of the line. Since this perfect line is identical to the line at the test port, the traveling waves are not reflected. What happens if the line standard, while uniform, is not identical to the test port? The problem is similar to one described in the previous section. In general, the question is impossible to answer, However, for illustration, we consider the approximation that v and i are continuous at the interface. In this case, we can compute the cascade matrix of the line of characteristic impedance $Z _ { l }$ as

$$
\Pi _ { 2 } ^ { \underline { { { 0 } } } } =
$$

$$
\frac { e ^ { + \gamma l } } { 1 - { \cal T } _ { 0 l } ^ { 2 } } \left[ \begin{array} { c c } { e ^ { - 2 \gamma l } - { \cal T } _ { 0 l } ^ { 2 } } & { ( 1 - e ^ { - 2 \gamma l } ) { \cal T } _ { 0 l } } \\ { - ( 1 - e ^ { - 2 \gamma l } ) { \cal T } _ { 0 l } } & { 1 - e ^ { - 2 \gamma l } { \cal T } _ { 0 l } ^ { 2 } } \end{array} \right] ,\tag{118}
$$

which can be transformed to

$$
\mathbb { T } _ { 2 } ^ { m m } =
$$

$$
\frac { e ^ { + \gamma l } } { 1 - \bar { I } _ { m l } ^ { 2 } } \left[ \begin{array} { c c } { e ^ { - 2 \gamma l } - \bar { I } _ { m l } ^ { 2 } } & { ( 1 - e ^ { - 2 \gamma l } ) \bar { I } _ { m l } } \\ { - ( 1 - e ^ { - 2 \gamma l } ) \bar { I } _ { m l } } & { 1 - e ^ { - 2 \gamma l } \bar { I } _ { m l } ^ { 2 } } \end{array} \right] .\tag{119}
$$

This is identical in form to the previous result for a perfect line standard. It leads to the result

$$
{ \cal Z } _ { \mathrm { \bar { \tau e f } } } ^ { m } = { \cal Z } _ { l } ~ .\tag{120}
$$

In this approximation, the reference impedance is the characteristic impedance of the line. This potentially useful result suggests that a particular line may be used as a calibration standard for any network analyzer with identical results. However, the assumption that v and i are continuous, which led to the result, is not generally valid. The example of a 50 Ω, 2.4 mm coaxial standard used on 50 $\Omega ,$ 3.5 mm coaxial test ports makes this clear, for the standard must reflect the traveling waves even though its characteristic impedance is appropriate for a reflectionless standard. In general, the quality of the approximation depends in detail on the nature of the waveguide interface.

Calibration using any of these devices, as long as $\mathbb { S } _ { 1 1 } ^ { 0 } = S _ { 2 2 } ^ { 0 }$ , leads to solutions differing only by a change of reference impedance. Of course, we can easily transform between any two reference impedances if given the values. A procedure to transform between LRL and LRM calibrations [16] is based on measuring the load reflection coefficient with respect to an LRL calibration. However, this is only a relative transformation; the initial and final reference impedances remain unknown. The most comprehensive procedure is to determine the absolute $\dot { Z } _ { \mathrm { r e f } } .$ A method to accomplish this combiņes the TRL calibration using a nominally perfect line with a measurement of $Z _ { 0 } ,$ which in this case is identical to $Z _ { \mathrm { r e f } }$ [12]. It is difficult to imagine determining the reference impedance of any of the other calibration methods, even in principle, without comparison to a TRL calibration.

Many calibration methods other than those based on the TRL algorithm are in use. These typically require the measurement of artifacts, such as open and short circuits, whose scattering parameters are presumed known. Although electromagnetic simulations may provide good estimates, the actual scattering parameters can be known accurately only by measurement. Thus the calibration artifacts must be viewed as transfer standards. If the scattering parameters are given incorrectly, the calibration may be inconsistent. However, if perfect short and open circuits are used along with a termination defined as a perfect match, it is possible to obtain a consistent calibration with the reference impedance equal to the load impedance of the termination.

## 4.2 Measurement of Pseudo-Waves and Waveguide Voltage and Current

The methods of the previous section provide for the measurement of ratios of pseudo-waves. In order to measure the wave amplitudes, an additional magnitude measurement is necessary. The most convenient parameter to measure is the power $P .$ From measurements of P and I' and a known $\mathbf { \mathcal { Z } } _ { \mathrm { r e f } } ,$ Eq. (59) allows the determination of lal. This applies to laol as well if we replace $Z _ { \mathrm { r e f } }$ by $Z _ { 0 } .$ The absolute phases of the pseudo-waves and traveling waves cannot be measured without specifying the arbitrary phase of the modal fields. However, the relative phase of a and b is given by Eq. (58).

Once a and b have been determined, lvl and lil are given by Eqs. (55) and (56). The ratio of these two equations determines the relative phase of v and i.

## 5. Alternative Circuit Theory Using Power Waves

In addition to the pseudo-waves a and b defined by Eqs. (53) and (54), other quantities may be defined using different linear combinations of v and i. Popular alternatives are the "incident and reflected wave amplitudes" normalized to “complex port numbers" [7]. For a complex port number $\hat { \boldsymbol { z } }$ these quantities are defined by

$$
\hat { a } ( \hat { Z } ) \equiv \frac { \upsilon + i \hat { Z } } { 2 \sqrt { \mathrm { R e } ( \hat { Z } ) } }
$$

and

(121)

$$
\hat { b } ( \hat { Z } ) \equiv { \frac { \upsilon - i \hat { Z } ^ { * } } { 2 \sqrt { \mathrm { R e } ( \hat { Z } ) } } } .\tag{122}
$$

In Ref. $[ 7 ] , \hat { z }$ is arbitrary except that $\mathbf { R e } ( \hat { Z } ) > 0 ;$ this resțriction is lifted in subsequent publications. When $\hat { \boldsymbol { z } }$ is the load impedance of the device connected to the port, a and b are known as power waves [8]. For simplicity, we shall use the term "power waves" for all quantities of the form (121) and (122).

We take v and i to be the waveguide voltage and current defined in Sec. 2. Like Ref. [7], we limit our discussion to the case $\mathbf { R e } ( \hat { Z } ) > 0$

When $\hat { z }$ is real, the power waves reduce to pseudo-waves (except for a phase factor) with reference impedance $\dot { \boldsymbol { Z } } _ { \mathrm { r e f } } = \dot { \boldsymbol { Z } }$ . Otherwise they do not correspond. The power waves are not equal to the traveling waves for any choice of $\hat { \boldsymbol { z } }$ unless the characteristic impedance is real. For example, Fig. 6 plots the power wave magnitudes corresponding to the example of Fig. 4; $\ddot { z }$ is chosen so that $\pmb { \hat { b } }$ vanishes at $z = 0 .$ This figure illustrates that the power waves are complicated functions of $z ;$ it is clearly unrealistic to interpret them as “incident and reflected waves."

The power waves are devised to satisfy the simple power relation

$$
p = | \hat { a } | ^ { 2 } - | \hat { b } | ^ { 2 }\tag{123}
$$

for any $\hat { \boldsymbol { z } }$ The pseudo-waves satisfy a relationship of this form only when $Z _ { \mathrm { r e f } }$ is real.

![](images/93229a1b378b39167a2386427d05af8173d29ac59bf3a3d1329ba5074aadc853.jpg)  
Fig. 6. The magnitudes of the power waves $\pmb { \hat { a } }$ and $\pmb { \hat { b } }$ for the example of Fig. 4. The characteristic impedance is taken to be 1−0.2j. Ż is chosen so that ${ \hat { T } } ( { \hat { Z } } )$ vanishes at the termination reference plane. Since the waves depend in a complicated fashion on z, $\hat { T } ( \hat { Z } )$ vanishes only at ${ z = } 0 .$

Power wave scattering parameters can be defined analogously to the pseudo-scattering parameters. For example, the power wave reflection coefficient is

$$
\hat { \cal { T } } ( \hat { Z } ) \equiv  { \frac { \hat { b } ( \hat { Z } ) } { \hat { a } ( \hat { Z } ) } } { = } { \frac { \upsilon - i \hat { Z } ^ { * } } { \upsilon + i \hat { Z } } } = { \frac { Z _ { \scriptscriptstyle { \mathrm { l o a d } } } - \hat { Z } ^ { * } } { Z _ { \scriptscriptstyle { \mathrm { l o a d } } } + \hat { Z } } } ,\tag{124}
$$

which should be contrasted to Eq. (95). The power wave reflection coefficient of an open circuit $( i = 0 )$ is equal to 1, the same as the pseudo-wave reflection coefficient defined earlier. However, the result for a short circuit $( \pmb { \nu } = 0 )$ is

$$
\upsilon = 0 \Rightarrow \hat { \cal { T } } ( \hat { \cal { Z } } ) = - \frac { \hat { \cal { Z } } ^ { \ast } } { \hat { \cal { Z } } } ,\tag{125}
$$

which is equal to the pseudo-wave refleçtion coefficient -1 only in the special case ${ \bf I m } ( \hat { Z } ) = 0$ This indicates clearly that the power waves are not generally related to the traveling waves by an impedance transform.

The implications of this are significant. For instance, the relationship between the load impedance and the pseudo-reflection coefficient is given by Eq. (95), which is the classical result. It is the basis of the Smith chart as well as most circuit design software. On the other hand, the equivalent relationship in terms of power wave quantities is Eq. (124), to which the Smith chart does not apply since it does not represent a linear fractional transformation. To sharpen this distinction, recall that the Smith chart is based on a normalized impedance; that is, the load impedance displayed on the chart is relative to $Z _ { \mathrm { r e f } }$ (Z0 in the case of traveling waves). The chart is able to accommodate the data in this form because the pseudo-reflection coefficient, as illustrated by Eq. (95), depends only on the ratio $\scriptstyle { Z _ { \mathrm { l o a d } } } / { Z _ { \mathrm { r e f } } } .$ The power wave reflection coefficient, however, depends not only on the ratio $Z _ { \mathrm { l o a d } } \hat { Z }$ but also on the phase of $\hat { \boldsymbol { z } }$ Therefore, an attempt to generalize the Smith chart to display power wave reflection coefficients must lead to a separate chart for each phase of $\hat { \boldsymbol { z } }$

Recall that the pseudo-wave scattering matrix of a reciprocal circuit is not generally symmetric in lossy waveguides. In contrast, advocates of power waves argue that the power wave scattering matrix of a lossy, reciprocal circuit is symmetric. For waveguide circuits, this is false. The usual derivation of symmetry makes use of the symmetry of the impedance matrix, which, as we have seen, does not hold for waveguides. Thus, one ubiquitous justification of a power wave description of waveguide circuits is invalid. The correct reciprocity relationship is given in Appendix D.

Although a complete circuit theory based on power waves is possible, we have chosen not to develop one, for several reasons. Unlike the power waves, the pseudo-waves are related to the traveling waves by an impedance transform and therefore avoid the problems discussed above.

Furthermore, unlike the power waves, the pseudowaves can generally be set equal to the traveling waves by an appropriate choice of the reference impedance. Although the pseudo-waves do not generally satisfy a simple power expression of the form Eq. (123), they can always be made to do so by an appropriate choice of the reference impedance. Typically this involves choosing $Z _ { \mathrm { r e f } }$ to be real, but the choice of $Z _ { \mathrm { r e f } } = Z _ { \mathrm { l o a d } } ,$ analogous to the choice $\hat { \boldsymbol Z } = \boldsymbol Z _ { \mathrm { l o a d } }$ made by Ref. [8], will also suffice.

Although a network analyzer may be used to measure power waves, such a use is rare for, as illustrated in the previous section, it is the pseudowaves that are measured using conventional calibration techniques. None of these methods may be easily modified to directly measure power waves. Methods which apply shorts and opens as calibration standards are inapplicable since only the open, not the short, is a useful power wave standard. Furthermore, the TRL method cannot be applied to power wave measurement since it is closely tied to the measurement of traveling waves.

One method of measuring a power wave reflection coefficient begins with first measuring the pseudo-wave reflection coefficient. If the reference impedance of that calibration can be determined, then the load impedance may be calculated from Eq. (96); the power wave reflection coefficient can then be determined from Eq. (124). Methods which do not require the determination of the pseudo-wave parameters as a prerequisite appear to be unknown at this time. In any case, such methods do not exist in the firmware which controls conventional network analyzers, so that these machines are incapable of determining power wave scattering parameters without external software.

## 6. Appendix A. Reduction of Maxwell's Equations

The electric and magnetic fields of a mode have been designated $e e ^ { - { \boldsymbol { r } } { \boldsymbol { z } } }$ and $\hbar e ^ { - \gamma z } .$ For the moment, we will allow anisotropy and therefore introduce the tensor permittivity e and tensor permeability ${ \pmb \mu } .$ Maxwell's equations take the form

$$
\begin{array} { r } { \nabla \times ( e e ^ { - \gamma z } ) = - j \omega \mu \cdot ( h e ^ { - \gamma z } ) , } \end{array}\tag{A1}
$$

$$
\begin{array} { r } { \nabla \times ( h e ^ { - \gamma z } ) = + j \omega \epsilon \cdot ( e e ^ { - \gamma z } ) , } \end{array}\tag{A2}
$$

$$
\nabla \cdot ( \epsilon \cdot e e ^ { - \gamma z } ) = 0 ,\tag{A3}
$$

and

$$
\nabla \cdot ( \mu \cdot h e ^ { - \gamma z } ) = 0 ,\tag{A4}
$$

which readily reduce to

$$
\nabla \times e - \gamma { z } \times e = - j \omega \mu \cdot h \ ,\tag{A5}
$$

$$
\begin{array} { r } { \nabla \times h - \gamma z \times h = + j \omega \epsilon \cdot e , } \end{array}\tag{A6}
$$

$$
\nabla \cdot ( \epsilon \cdot e ) = \gamma ( \epsilon \cdot e ) \cdot z \ ,\tag{A7}
$$

and

$$
\begin{array} { r } { \nabla \cdot ( \pmb { \mu } \cdot \pmb { h } ) = \gamma ( \pmb { \mu } \cdot \pmb { h } ) \cdot \pmb { z } . } \end{array}\tag{A8}
$$

If we now divide e and h into their transverse and axial components, Eqs. (A5) and (A6) become

$$
\begin{array} { r } { \nabla \times \boldsymbol { e } _ { i } = - j \omega ( \pmb { \mu } \cdot \pmb { h } ) \cdot \boldsymbol { z } , } \end{array}\tag{A9}
$$

$$
\nabla \times h _ { t } = + j \omega ( \epsilon \cdot e \bf { \tau } ) \cdot z\tag{A10}
$$

$$
\boldsymbol { z } \times \nabla \boldsymbol { e } _ { z } + \gamma \boldsymbol { z } \times \boldsymbol { e } _ { t } = + j \omega \left( \boldsymbol { \mu } \cdot \boldsymbol { h } \right) _ { t } ,\tag{A11}
$$

and

$$
\begin{array} { r } { z \times \nabla h _ { z } + g z \times h _ { t } = - j \omega ( \epsilon \cdot e ) _ { t } . } \end{array}\tag{A12}
$$

For the isotropic materials discussed in the text, Eqs. (A7)-(A12) reduce to Eqs. $( 2 ) - ( 7 )$ . In general, it appears difficult to generalize the text to include materials of arbitrary anisotropy. However, generalization is fairly simple in the absence of terms in e and μ coupling between transverse and axial field components. In that case, we can write

$$
\epsilon = \epsilon _ { t } + \epsilon _ { z } z z ; z \cdot \epsilon _ { t } = \epsilon _ { t } \cdot z = 0\tag{A13}
$$

and

$$
\begin{array} { r } { \mu = \mu _ { t } + \mu _ { z } z z ; z \cdot \mu _ { t } = \mu _ { t } \cdot z = 0 . } \end{array}\tag{A14}
$$

All of the results in the text follow with slight modification. For example, equations Eqs. (B5) and (B6), from which the circuit parameter expressions arise, must be modified by the following replacements:

$$
\epsilon | e _ { t } | ^ { 2 } \to e _ { t } { ^ { * } } \cdot \epsilon _ { t } \cdot e _ { t } ,\tag{A15}
$$

$$
\mu | \dot { \pmb { h } } _ { t } | ^ { 2 }  \dot { \pmb { h } } _ { t } ^ { * } \cdot \pmb { \mu } _ { t } \cdot \pmb { h } _ { t } ,\tag{A16}
$$

$$
\epsilon | e _ { z } | ^ { 2 }  \epsilon _ { z } | e _ { z } | ^ { 2 } ,\tag{A17}
$$

and

$$
\mu | h _ { z } | ^ { 2 }  \mu _ { z } | h _ { z } | ^ { 2 } .\tag{A18}
$$

## 7. Appendix B. Circuit Parameter Integral Expressions

Taking the scalar product of both sides of Eq. (5) with $z \times e _ { t } ^ { * }$ results in

$$
\gamma z \cdot e _ { t } ^ { * } \times h _ { t } + z \cdot e _ { t } ^ { * } \times \nabla h _ { z } =
$$

$$
\begin{array} { r } { + j \omega \epsilon ( z \times e _ { t } { * } ) \cdot ( z \times e _ { t } ) = + j \omega \epsilon | e _ { t } | ^ { 2 } . } \end{array}\tag{B1}
$$

Integrating over the cross section of the waveguide and recognizing the first integral as $p _ { 0 } { } ^ { * } = | \boldsymbol { v } _ { 0 } | ^ { 2 } / \bar { Z } _ { 0 } ,$ we have

$$
\frac { \gamma } { Z _ { 0 } } = \frac { 1 } { | \boldsymbol { v } _ { 0 } | ^ { 2 } } \left[ j \omega \int _ { S } \boldsymbol { \epsilon } | \boldsymbol { e } _ { t } | ^ { 2 } \mathrm { d } S - z \cdot \int _ { S } \boldsymbol { e } _ { t } \ast \boldsymbol { \nabla } h _ { z } \mathrm { d } S \right] .\tag{B2}
$$

The second integral can be manipulated into a simpler form. First apply Stokes's Law to the vector $\hat { h } _ { z } \pmb { e } _ { I } ^ { * }$ to yield

$$
\int _ { S } \nabla \times \left( h _ { z } { e _ { i } } ^ { * } \right) \cdot z \mathrm { d } S = \int _ { S } h _ { z } \nabla \times { e _ { t } } ^ { * } \cdot z \mathrm { d } S -
$$

$$
\int _ { S } { e _ { t } } ^ { * } \times \nabla \hbar _ { z } \cdot { z } \mathrm { d } S = \int _ { \partial S } h _ { z } \boldsymbol { e _ { t } } ^ { * } \cdot \mathrm { d } \boldsymbol { l } ,\tag{B3}
$$

where ∂S is the boundary of S and dl is a line element along that boundary. If the waveguide is transversely closed by a perfectly conducting boundary, then S coincides with that boundary and the line integral vanishes. If the waveguide is open, then a portion of S may lie at infinity, but the integral also vanishes as long as e, vanishes fast enough to ensure that the modal power is finite. Finally, although Stokes' Law cannot formally be applied across material discontinuities, it can readily be shown that the line integrals on both sides of the boundary are equal and opposite. As a result, the line integral in Eq. (B3) vanishes. The insertion of Eq. (2) simplifies Eq. (B3) to

$$
\boldsymbol { z } \cdot \int _ { S } \boldsymbol { e } _ { t } \cdot \boldsymbol { \times } \nabla h _ { z } \mathrm { d } S = \int _ { S } h _ { z } \nabla \times \boldsymbol { e } _ { t } \cdot \boldsymbol { \cdot } \boldsymbol { z } \mathrm { d } S =
$$

$$
j \omega \int _ { S } \mu ^ { * } | h _ { z } | ^ { 2 } \mathrm { d } S ,\tag{B4}
$$

so Eq. (B2) becomes

$$
\frac { \gamma } { Z _ { 0 } } = \frac { j \omega } { | \boldsymbol { u } _ { 0 } | ^ { 2 } } \bigg [ \int _ { S } \boldsymbol { \epsilon } | \boldsymbol { e } _ { t } | ^ { 2 } \mathrm { d } S - \int _ { S } \boldsymbol { \mu } ^ { * } | \boldsymbol { h } _ { z } | ^ { 2 } \mathrm { d } S \bigg ] .\tag{B5}
$$

By an analogous procedure using Eqs. (3) and (4), we may demonstrate that

$$
\gamma Z _ { 0 } { = } \frac { j \omega } { \left| \dot { \iota } _ { 0 } \right| ^ { 2 } } \left[ \int _ { S } \mu \big | h _ { t } \big | ^ { 2 } \mathrm { ~ d } S - \int _ { S } \epsilon ^ { * } \big | e _ { z } \big | ^ { 2 } \mathrm { ~ d } S \right] .\tag{B6}
$$

The use of Eqs. (B5) and (B6) along with definitions (29) and (30) results in Eqs. (33)–(36) for the circuit parameters C, L, G, and R.

8. Appendix C. Relations Between ${ \pmb p } { \pmb 0 }$ and γ

From Eqs. (20), (29), and (30),

$$
\gamma p _ { 0 } { } ^ { * } = | \mathbf { \boldsymbol { u } } _ { 0 } | ^ { 2 } \left[ j \omega C + G \right]\tag{C1}
$$

and

$$
\gamma p _ { 0 } = | i _ { 0 } | ^ { 2 } [ j \omega L + R ] ,\tag{C2}
$$

from which it can readily be shown that

$$
\begin{array} { r } { 2 \mathrm { R e } ( \gamma ) \ \mathrm { R e } ( p _ { 0 } ) = + | \upsilon _ { 0 } | ^ { 2 } G + | i _ { 0 } | ^ { 2 } R \ , } \end{array}\tag{C3}
$$

$$
\begin{array} { r } { 2 \mathrm { R e } ( \gamma ) \ \mathrm { I m } ( p _ { 0 } ) = - | \nu _ { 0 } | ^ { 2 } \ \omega C + | i _ { 0 } | ^ { 2 } \omega L , } \end{array}\tag{C4}
$$

$$
\begin{array} { r } { 2 \mathrm { I m } ( \gamma ) \ \mathrm { R e } ( p _ { 0 } ) = + | \nu _ { 0 } | ^ { 2 } \ \omega C + | i _ { 0 } | ^ { 2 } \omega L , } \end{array}\tag{C5}
$$

and

$$
2 \mathrm { I m } ( \gamma ) \mathrm { I m } ( p _ { 0 } ) = + | \psi _ { 0 } | ^ { 2 } G - | i _ { 0 } | ^ { 2 } R .\tag{C6}
$$

An interesting alternative form of Eq. (C5) is

$$
\mathrm { R e } ( p _ { 0 } ) = \frac { \omega } { \beta } \left[ \frac { 1 } { 2 } | \upsilon _ { 0 } | ^ { 2 } C + \frac { 1 } { 2 } | i _ { 0 } | ^ { 2 } L \right] .\tag{C7}
$$

This is the real average power carried by the forward mode at ${ z = } 0 ,$ For TEM modes, it is the product of the group velocity $\omega / \beta$ and the energy density (per unit length), represented by the term in brackets.

If the materials are lossless, then certain useful results apply. In that case, lul² ${ \cal G } = \{ i _ { 0 } | ^ { 2 } { \cal R } = 0$ Aside from the degenerate case in which ${ \mathcal { P } } \mathfrak { 0 } { = } 0 ,$ only two sorts of modes may exist. The first, which we denote propagating modes, satisfy

$$
\begin{array} { r } { \mathrm { R e } ( \gamma ) = \mathrm { I m } ( p _ { 0 } ) = \mathrm { I m } ( Z _ { 0 } ) = 0 ; } \end{array}
$$

$$
\mathrm { I m } ( \gamma ) { \neq } 0 ; \ \mathrm { R e } ( p _ { 0 } ) > 0 ,\tag{C8}
$$

which implies that they propagate without decay with a real characteristic impedance. Equation (C4) becomes

$$
\begin{array} { r } { \left( \mathrm { R e } ( \gamma ) = 0 \right) \Rightarrow | \nu _ { 0 } | ^ { 2 } C = | i _ { 0 } | ^ { 2 } L , } \end{array}\tag{C9}
$$

leaving free only one of the four parameters $R , c$ G, and L. Equation (C9) can be expanded as

$$
( \operatorname { R e } ( \gamma ) = 0 ) \Rightarrow \int _ { s } \mu | h | ^ { 2 } \mathrm { d } S = \int _ { s } \epsilon | e | ^ { 2 } \mathrm { d } S .\tag{C10}
$$

This states the well-known result [3] that the energy in a lossless propagating wave is divided equally between the electric and magnetic fields.

Modes in lossless media with $\yen 020$ that are not propagating satisfy

$$
\mathrm { I m } ( \gamma ) = \mathrm { R e } ( p _ { 0 } ) = \mathrm { R e } ( Z _ { 0 } ) = 0 ;
$$

$$
\begin{array} { r } { \mathbf { R e } ( \gamma ) > 0 ; \mathbf { I m } ( p _ { 0 } ) \neq 0 , } \end{array}\tag{C11}
$$

and therefore

$$
| { \boldsymbol { v } } _ { 0 } | ^ { 2 } C = - | i _ { 0 } | ^ { 2 } L .\tag{C12}
$$

These modes are purely evanescent, decaying exponentially and, in isolation, carrying no real power. The inductance and capacitance are of opposite sign.

If we restrict ourselves to passive but not necessarily lossless media, certain converse results apply. Passivity ensures that G and R are nonnegative. Thus, if either $\mathbf { R e } ( y ) { = } 0$ or $\mathtt { R e } ( p _ { 0 } ) = 0 ,$ then Eq. (C3) requires $\lvert \mathbf { \boldsymbol { v } } _ { 0 } \rvert ^ { 2 } G = \lvert \dot { t } _ { 0 } \rvert ^ { 2 } R = 0 .$ Since $\pmb { \epsilon } ^ { \prime \prime }$ and $\mu ^ { \prime \prime }$ are nonnegative in passive media, Eqs. (35) and (36)

require that $\epsilon ^ { \prime \prime } e = \mu ^ { \prime \prime } h = 0$ everywhere. Now, if ${ \pmb e } = { \bf 0 } _ { ; }$ , then Maxwell's equations imply that $\pmb { h } = \pmb 0$ (and vice versa), except in the case ${ \pmb \omega } = { \bf 0 } ,$ which we have explicitly excluded. Therefore, in passive media, the possibilities $\mathtt { R e } ( y ) { = } 0$ (unattenuated mode) or $\mathtt { R e } ( p _ { 0 } ) = 0$ (mode carrying no real power) occur only if $\epsilon ^ { \prime \prime } { = } \mu ^ { \prime \prime } { = } 0 ;$ that is, only when the media are lossless. In contrast, there is no apparent prohibition against Im(γ) or Im(po) vanishing in lossy media.

Finally, we treat the degenerate modes in which either γ or ${ p } _ { 0 }$ vanishes. From Eqs. (C1) and (C2), these modes satisfy

$$
\{ \gamma p _ { 0 } = 0 \} \Rightarrow | { \boldsymbol { v _ { 0 } } } | ^ { 2 } C = | { \boldsymbol { v _ { 0 } } } | ^ { 2 } G = | i _ { 0 } | ^ { 2 } L = | i _ { 0 } | ^ { 2 } R = 0 .\tag{C13}
$$

The second and fourth conditions ensure that such degeneracy occurs only in lossless waveguides.

if $\gamma = 0 ,$ then Maxwell's equations decouple into one set [Eqs. (2), (5), and (6)] involving only e, and $\hslash _ { z }$ and another set [Eqs. (3), (4), and (7)] involving only $\mathbf { { \pmb { h } } } _ { t }$ and $\scriptstyle e _ { z }$ Therefore, we can decompose the fields into modes with either $e _ { t } = h _ { z } = 0$ or $\pmb { h } _ { t } = \pmb { e } _ { z } = \pmb { 0 }$ . In the former case, $| \boldsymbol { v } _ { \mathrm { 0 } } | ^ { 2 } C$ automatically vanishes, due to Eq. (33), and the condition $| \dot { \bar { t } } _ { 0 } | ^ { 2 } L = 0$ constrains the remaining fields; the opposite holds true in the latter case. In either situation, $p _ { 0 } { = } 0$ since the Poynting vector $\pmb { e } _ { 1 } \times \pmb { h } _ { 1 }$ vanishes. In this case $\gamma = \boldsymbol { p _ { 0 } = 0 }$ , exemplified by a lossless waveguide mode operating exactly at the cutoff frequency, the forward and backward modes are indistinguishable.

On the other hand, $p _ { 0 } = 0$ does not imply that $\gamma = 0 .$ Furthermore, in contrast to the lossless case with $p _ { 0 } { \not = } 0$ discussed above, $\pmb { \gamma }$ is not restricted to be real or imaginary. "Complex waves," in which γ is neither real nor imaginary even though the materials are lossless, have been discovered in inhomogeneous as well as in anisotropic media. They are discussed in Ref. [20] and references included therein.

## 9. Appendix D. Reciprocity Relations

Consider two sets of electromagnetic fields $( E ^ { \prime } , H ^ { \prime } )$ and $( E ^ { \prime \prime } , H ^ { \prime \prime } )$ , which are produced by two different sets of boundary conditions. Applying the divergence theorem to $\dot { \pmb { E } ^ { \prime } } \times \pmb { H } ^ { \prime }$ and using the homogeneous Maxwell's equations produces the wellknown result that

$$
\int { \big ( } E ^ { \prime } \times H ^ { \prime \prime } - E ^ { n } \times H ^ { \prime } { \big ) } \cdot n \ \mathrm { d } S = 0 ,\tag{D1}
$$

whenever the permittivity and permeability tensors are symmetric. In Eq. (D1), the surface encloses a closed region and the unit vector n is the outward normal to the surface. We let the surface enclose an entire waveguide junction and become infinitely large in such a way that the contributions to the integral can be entirely accounted for by the single mode of interest propagating in each waveguide leaving the junction. Expressing the fields in each port n in terms of Eqs. (12) and (13), Eq. (D1) becomes

$$
\sum _ { n } \frac { v _ { n } { } ^ { \prime } \dot { i } _ { n } ^ { \prime \prime } } { v _ { 0 n } \dot { i } _ { 0 n } } \ \widetilde { p } _ { 0 n } = \sum _ { n } \frac { v _ { n } { } ^ { \prime \prime } \dot { i } _ { n } ^ { \prime } } { v _ { 0 n } \dot { i } _ { 0 n } } \ \widetilde { p } _ { 0 n } ,\tag{D2}
$$

having defined

$$
\widetilde { \boldsymbol { p } } _ { 0 n } \equiv \int _ { S _ { n } } \boldsymbol { e } _ { i n } \times \boldsymbol { h } _ { i n } \cdot \boldsymbol { z } \ \mathrm { d } S ,\tag{D3}
$$

where ${ \pmb S } _ { \pmb n }$ is the cross section of the nth waveguide. Equation (D2) can be written as the matrix equation

$$
\mathsf { i } ^ { \prime \prime } \mathsf { W } \mathsf { v } ^ { \prime } = \mathsf { v } ^ { \prime \prime } \mathsf { W } \mathsf { i } ^ { \prime } .\tag{D4}
$$

As before, i and v are column vectors of $i _ { n }$ and ${ \pmb v } _ { \pmb n ; \pmb \mathrm { \Sigma } }$ and $" \ell > "$ stands for "transpose." W is the diagonal matrix

$$
\begin{array} { r } { \mathsf { W } \equiv \mathrm { d i a g } ( \mathsf { W } _ { n } ) ; \mathsf { W } _ { n } \equiv \frac { \widetilde { p } _ { 0 n } } { { \upsilon _ { 0 n } } i _ { 0 n } } = \frac { { \upsilon } _ { 0 n } ^ { * } } { { \upsilon } _ { 0 n } } \frac { \widetilde { p } _ { 0 n } } { \widetilde { p } _ { 0 n } ^ { * } } , } \end{array}\tag{D5}
$$

where Eq. (20) has been used. Inserting ${ \pmb v } = { \pmb Z } { \mathbb 1 }$ into Eq. (D4) and requiring that the result holds for all values of i’ and $\mathsf { i } ^ { \bar { \prime } } ,$ we determine that

$$
{ \cal Z } ^ { \dagger } = \mathsf { W } { \cal Z } \mathsf { W } ^ { - 1 } ,\tag{D6}
$$

which is the reciprocity requirement on the impedance matrix. It requires that the elements of Z satisfy

$$
{ Z _ { n m } } = \frac { { \sf W } _ { m } } { \sf W _ { n } } \ : { Z _ { m n } } \ : .\tag{D7}
$$

To determine the analogous condition on $\mathsf { \pmb { s } } ,$ take the transpose of Eq. (E5):

$$
\bar { \mathsf { S } } ^ { \mathrm { t } } = \mathsf { U } ^ { - 1 } ( \bar { Z } ^ { \mathrm { t } } + \bar { Z } _ { r e \mathrm { f } } ) ^ { - 1 } ( \bar { Z } ^ { \mathrm { t } } - \bar { Z } _ { r e \mathrm { f } } ) \mathsf { U } .\tag{D8}
$$

Insert Eq. (D6) and factor out W and $\ W ^ { - 1 }$ , noting that W $Z _ { \mathrm { r e f } } \ : \mathsf { W } ^ { - 1 } = Z _ { \mathrm { r e f } }$ since W and $Z _ { \theta \uparrow }$ are diagonal. The result is

$$
S ^ { \mathrm { t } } = \mathsf { U } ^ { - 1 } \mathsf { W } ( \mathsf { Z } + \mathsf { Z } _ { \mathrm { r e f } } ) ^ { - 1 } \mathsf { \Omega } ( \mathsf { Z } - \mathsf { Z } _ { \mathrm { r e f } } ) \mathsf { W } ^ { - 1 } \mathsf { U } .\tag{D9}
$$

The two central terms can be commuted using the fact that any matrices A and B satisfy

$$
( \mathsf { A } + \mathsf { B } ) ^ { - 1 } ( \mathsf { A } - \mathsf { B } ) = \mathsf { B } ^ { - 1 } ( \mathsf { A } - \mathsf { B } ) ( \mathsf { A } + \mathsf { B } ) ^ { - 1 } \mathsf { B }\tag{D10}
$$

as long as the inverses exist. Using Eq. (D10) in Eq. (D9) and using Eq. (E5) to express the result in terms of S, we have

$$
S ^ { 1 } { = } P ^ { - 1 } S P ,\tag{D11}
$$

using the definition

$$
\begin{array} { r } { \mathsf { P } \equiv \mathsf { Z } _ { \mathrm { e f } } \mathsf { U } ^ { 2 } \mathsf { W } ^ { - 1 } . } \end{array}\tag{D12}
$$

Since P is diagonal, Eq. (D11) requires that the elements of S satisfy

$$
\mathsf { S } _ { n m } = \frac { \mathsf { P } _ { n n } } { \mathsf { P } _ { m m } } \mathsf { S } _ { m n } ,\tag{D13}
$$

which is expressed more explicitly as Eq. (64) of the text.

We can also develop a reciprocity relation for the power wave scattering matrix, defined by

$$
\hat { \boldsymbol { \mathsf { b } } } = \hat { \mathsf { S } } \hat { \mathsf { a } } ,\tag{D14}
$$

where

$$
\hat { \mathbf { a } } = \mathsf { F } ( \mathsf { v } + \hat { \mathbf { Z } } )\tag{D15}
$$

and

$$
\hat { \mathsf { b } } = \mathsf { F } ( \mathsf { v } - \hat { \mathsf { Z } } ^ { * } \mathsf { i } )\tag{D16}
$$

are the vector forms of Eqs. (121) and (122). We have defined

$$
\hat { { \sf z } } \equiv { \tt d i a g } \left( \hat { { \cal z } } \right)\tag{D17}
$$

and

$$
\mathsf { F } \equiv \mathrm { d i a g } \left( \frac { 1 } { 2 \sqrt { \hat { z } } } \right) .\tag{D18}
$$

Inserting Eqs. (D15) and (D16), as well as ${ \pmb v } = { \pmb Z } { \dag } ,$ into Eq. (D14) and insisting that the result hold for all i yields

$$
\hat { \mathbb S } = \mathsf { F } ( \mathsf { Z } - \hat { \mathsf { Z } } ^ { \ast } ) ( \mathsf { Z } + \hat { \mathsf { Z } } ) ^ { - 1 } \mathsf { F } ^ { - 1 } ,\tag{D19}
$$

the transpose of which is

$$
\hat { \mathsf { S } } ^ { ! } = \mathbb { F } ^ { - 1 } ( \mathsf { Z } ^ { ! } + \hat { \mathsf { Z } } ) ^ { - 1 } ( \mathsf { Z } ^ { ! } - \hat { \mathsf { Z } } ^ { * } ) \mathsf { F } .\tag{D20}
$$

Using Eq. (D6) and some simple manipulation leads to

$$
\hat { \mathsf { S } } ^ { \iota } { = } \mathsf { F } ^ { - 1 } \mathsf { W } ( \mathsf { Z } { + } \hat { \mathsf { Z } } ) ^ { - 1 } ( \mathsf { Z } { - } \hat { \mathsf { Z } } ^ { * } ) \mathsf { W } ^ { - 1 } \mathsf { F } .\tag{D21}
$$

Reference [8] shows that

$$
\begin{array} { r } { ( \mathsf { Z } + \hat { \mathsf { Z } } ) ^ { - 1 } \left( \mathsf { Z } - \hat { \mathsf { Z } } ^ { * } \right) = \qquad } \\ { \qquad \mathsf { F } ^ { 2 } ( \mathsf { Z } - \hat { \mathsf { Z } } ^ { * } ) ( \mathsf { Z } + \hat { \mathsf { Z } } ) ^ { - 1 } \mathsf { F } ^ { - 2 } = \mathsf { F } \hat { \mathsf { S } } \mathsf { F } ^ { - 1 } , } \end{array}\tag{D22}
$$

so that Eq. (D21) reduces to the simple result

$$
\hat { \mathsf { S } } ^ { 1 } = \mathsf { W } \hat { \mathsf { S } } \mathsf { W } ^ { - 1 }\tag{D23}
$$

The power wave scattering matrix therefore obeys a reciprocity relation identical to the one (D6) satisfied by the impedance matrix. In lossy waveguides, neither is generally symmetric.

## 10. Appendix E. Relations Between Z and S

Recall that a, b, v, and i are defined as column vectors whose elements are $a _ { m } , b _ { m } , \upsilon _ { m }$ , and $i _ { m }$ at the various waveguide ports m. The vector representation of Eqs. (53) and (54) are

$$
\mathsf { a } { = } \frac 1 2 \mathsf { U } ( \mathsf { v } + \mathsf { Z } _ { \mathsf { r o f } } \mathsf { i } )
$$

and

(E1)

$$
\mathsf { b } = \frac 1 2 \mathsf { U } \left( \mathsf { v } - \mathsf { Z } _ { \mathsf { r o t } } \mathsf { i } \right) ,\tag{E2}
$$

where U is a diagonal matrix defined by

$$
\mathsf { U } \equiv \mathrm { d i a g } \left( \frac { \left| v _ { 0 m } \right| } { \upsilon _ { \mathsf { m } } } \frac { \sqrt { \mathsf { R e } ( Z _ { \mathrm { r e f } } ^ { m } ) } } { Z _ { \mathrm { r e f } } ^ { m } } \right) .\tag{E3}
$$

Inserting ${ \pmb v } = { \pmb Z } { \dag }$ into Eqs. (E1) and (E2) eliminates v. The condition b=Sa then implies

$$
\mathsf { b } = \frac { 1 } { 2 } \mathsf { U } \left( \mathsf { Z } - \mathsf { Z } _ { \mathsf { r e f } } \right) \mathsf { i } = \mathsf { S } \mathsf { a } = \frac { 1 } { 2 } \mathsf { S } \mathsf { U } \left( \mathsf { Z } + \mathsf { Z } _ { \mathsf { r e f } } \right) \mathsf { i } .\tag{E4}
$$

Since this must hold for all ${ \mathfrak { i } } ,$ we can solve for S, yielding

$$
\begin{array} { r l } & { \bar { \mathsf { S } } = \mathsf { U } \left( \bar { Z } - \bar { Z } _ { \mathsf { r e f } } \right) \left( \bar { Z } + \bar { Z } _ { \mathsf { r e f } } \right) ^ { - 1 } \mathsf { U } ^ { - 1 } = } \\ & { } \\ & { \mathsf { U } ( \bar { Z } Z _ { \mathsf { r e f } } ^ { - 1 } - 1 ) \left( \bar { Z } Z _ { \mathsf { r e f } } ^ { - 1 } + 1 \right) ^ { - 1 } \mathsf { U } ^ { - 1 } . } \end{array}\tag{E5}
$$

This can be easily inverted to produce

$$
\mathsf { Z } = ( \mathsf { I } - \mathsf { U } ^ { - 1 } \mathsf { S } \mathsf { U } ) ^ { - 1 } ( \mathsf { I } + \mathsf { U } ^ { - 1 } \mathsf { S } \mathsf { U } ) \mathsf { Z } _ { \mathsf { I } \mathsf { 0 } \mathsf { I } } .\tag{E6}
$$

## 11. Appendix F. Renormalization Table

The text allows for the arbitrarily normalization of the parameters ${ \pmb e } _ { t }$ and ${ \mathfrak { u } } _ { 0 } .$ This table details the effects of renormalizing these two parameters on the remaining variables. The second column shows the effect on the element in the first column of multiplying $e _ { t }$ by the factor $\pmb { \alpha } .$ The third column shows the results of a change in the voltage integration path which multiplies $\pmb { \nu _ { 0 } }$ by the factor $\beta ,$ No result is shown if the variable is independent of the normalization.

Renormalization table
<table><tr><td> $\pmb { \gamma }$   $\mathbf { } _ { E _ { i } , H _ { i } }$ </td><td></td><td></td></tr><tr><td> $\mathbf { } _ { e _ { i } , h _ { i } }$ </td><td> $\alpha e _ { i } , \alpha h _ { i }$ </td><td></td></tr><tr><td> $c _ { \star } , c _ { \star }$ </td><td> ${ \mathsf { c } } _ { + } / \alpha , { \mathsf { c } } _ { - } / \alpha$ </td><td></td></tr><tr><td> ${ \pmb v } _ { \pmb { 0 } }$ </td><td> $\pmb { \alpha } \pmb { \nu } _ { 0 }$ </td><td> $\beta \mathbf { { u } _ { 0 } }$ </td></tr><tr><td> $i _ { 0 }$ </td><td> $\pmb { c } \pmb { i } _ { 0 }$ </td><td> $i _ { 0 } / \beta ^ { \ast }$ </td></tr><tr><td> $\pmb { \nu }$ </td><td></td><td> $\beta \nu$ </td></tr><tr><td> $\pmb { i }$ </td><td></td><td> $i / \beta ^ { * }$ </td></tr><tr><td> ${ \pmb p _ { 0 } }$ </td><td> $| \alpha | ^ { 2 } p _ { 0 }$ </td><td></td></tr><tr><td> $\pmb { p }$ </td><td></td><td></td></tr><tr><td> $\pmb { P }$ </td><td></td><td></td></tr><tr><td> ${ \pmb Z } _ { \pmb { 0 } }$ </td><td></td><td> $| \beta | ^ { 2 } Z _ { 0 }$ </td></tr><tr><td> $C , G$ </td><td></td><td> $C / | \beta | ^ { 2 } , G / | \beta | ^ { 2 }$ </td></tr><tr><td> $L , R$ </td><td></td><td> $\vert \beta \vert ^ { 2 } L , \vert \beta \vert ^ { 2 } R$ </td></tr><tr><td> $a _ { 0 } , b _ { 0 }$ </td><td> $\frac { | \alpha | } { \alpha } a _ { 0 } , \frac { | \alpha | } { \alpha } b _ { 0 }$ </td><td></td></tr><tr><td> $a ( Z _ { \mathrm { r e f } } ) , b ( Z _ { \mathrm { r e f } } )$ </td><td> $\frac { \left| \alpha \right| } { \alpha } a \left( Z _ { \mathrm { r e f } } \right) , \frac { \left| \alpha \right| } { a } b \left( Z _ { \mathrm { r e f } } \right)$ </td><td> $\alpha ( Z _ { \mathrm { r e f } } / _ { | \beta | ^ { 2 } } ) , b ( Z _ { \mathrm { r e f } } / _ { | \beta | ^ { 2 } } )$ </td></tr><tr><td> $\widetilde { p } _ { \mathfrak { v } }$ </td><td> $\alpha ^ { 2 } \widetilde { p } _ { 0 }$ </td><td></td></tr><tr><td> $\pmb { K _ { n } }$ </td><td> $\Big ( \frac { \alpha } { | \alpha | } \Big ) ^ { 2 } K _ { n }$ </td><td></td></tr><tr><td> $W _ { n }$ </td><td></td><td> $\frac { \beta ^ { * } } { \beta } W _ { n }$ </td></tr><tr><td> $\tilde { S _ { i j } } ^ { 0 }$ </td><td> $\frac { | \alpha _ { i } | } { \alpha _ { l } } \frac { \alpha _ { j } } { | \alpha _ { j } | } S _ { i j } ^ { 0 }$ </td><td></td></tr><tr><td> $S _ { i j } ( Z _ { \mathrm { r e f } } ^ { i } , \ Z _ { \mathrm { r e f } } ^ { j } )$ </td><td> $\frac { \left| \alpha _ { i } \right| } { \alpha _ { i } } \frac { \alpha _ { i } } { \left| \alpha _ { j } \right| } S _ { i j } \left( Z _ { \mathrm { r e f } } ^ { i } , Z _ { \mathrm { r e f } } ^ { j } \right)$ </td><td> $S _ { i j } ( Z _ { \mathrm { r e f } } ^ { i } / _ { | \beta _ { i } | ^ { 2 } } , \ Z _ { \mathrm { r e f } } ^ { j } / _ { | \beta _ { j } | ^ { 2 } } )$ </td></tr><tr><td> $\pmb { { \cal T } _ { 0 } }$ </td><td></td><td> $T ( Z _ { \mathrm { r e f } } / _ { | \beta | ^ { 2 } } )$ </td></tr><tr><td> $T ( Z _ { \tt r e f } )$ </td><td></td><td> $\beta _ { i } \beta _ { j } ^ { * } Z _ { i j }$ </td></tr><tr><td> $\boldsymbol { Z } _ { I J }$ </td><td></td><td> $| \beta | ^ { 2 } Z _ { \mathrm { l o o d } }$ </td></tr><tr><td> $\scriptstyle z _ { \mathrm { l o o d } }$ </td><td></td><td></td></tr><tr><td> $\gamma _ { i j }$ </td><td></td><td> $Y _ { i j } / ( \beta _ { \mathrm { i } } ^ { * } \beta _ { j } )$ </td></tr><tr><td> ${ \pmb R } ^ { 0 }$ </td><td> $\frac { \left| \alpha _ { 1 } \right| } { \alpha _ { 1 } } \frac { \alpha _ { 2 } } { \left| \alpha _ { 2 } \right| } \mathsf { R } ^ { 0 }$ </td><td></td></tr><tr><td> $\mathsf { R } ( Z _ { \mathrm { r e f } } ^ { 1 } , \ : Z _ { \mathrm { r e f } } ^ { 2 } )$ </td><td> $\frac { \left| \alpha _ { 1 } \right| } { \alpha _ { 1 } } \frac { \alpha _ { 2 } } { \left| \alpha _ { 2 } \right| } \mathsf { R } ( Z _ { \mathrm { r e f } } ^ { 1 } , Z _ { \mathrm { r e f } } ^ { 2 } )$ </td><td> $\mathsf { R } ( Z _ { \mathrm { r e f } } ^ { 1 } / _ { | \beta _ { 1 } | ^ { 2 } } , Z _ { \mathrm { r e f } } ^ { 2 } / _ { | \beta _ { 2 } | ^ { 2 } } )$ </td></tr></table>

## Acknowledgments

The authors appreciate the contributions of Prof. Robert E. Collin and Dr. David A. Hill, both of whom read the manuscript and offered critical suggestions.

## 12. References

[1] C. G. Montgomery, R. H. Dicke, and E. M. Purcell, eds., Principles of Microwave Circuits, New York, McGraw-Hill (1948).

[2] N. Marcuvitz, Waveguide Handbook, New York, McGraw-Hill (1951).

[3] R. E. Collin, Foundations for Microwave Engineering, New York, McGraw-Hill (1966).

[4] D. M. Kerns and R. W. Beatty, Basic Theory of Waveguide Junctions and Introductory Microwave Network Analysis, Oxford, Pergamon Press (1967).

[5] F. E. Gardiol, Lossy Transmission Lines, Norwood, Ma, Artech House (1987).

[6] J. R. Brews, Transmission Line Models for Lossy Waveguide Interconnections in VLSI, IEEE Trans. Electron Devices ED-33, 1356–1365 (1986).

[7] D. C. Youla, On Scattering Matrices Normalized to Complex Port Numbers, Proc. IRE 49, 1221 (1961).

[8] K. Kurokawa, An Introduction to the Theory of Microwave Circuits, New York, Academic Press (1969).

[9] R. F. Harrington, Time-Harmonic Electromagnetic Fields, New York, McGraw-Hill (1961) pp. 17–20.

[10] J. R. Brews, Characteristic Impedance of Microstrip Lines, IEEE Trans. Microwave Theory Tech. MTT-35, 30–34 (1987).

[11] S. A. Schelkunoff, Impedance Concept in Wave Guides, Quart. Appl. Math. 2, 1–14 (1944).

[12] R. B. Marks and D. F. Williams, Characteristic Impedance Determination Using Propagation Constant Measurement, IEEE Microwave Guided Wave Lett. 1, 141– 143 (1991)

[13] D. F. Williams and R. B. Marks, Transmission Line Capacitance Measurement, IEEE Microwave Guided Wave Lett. 1, 243–245 (1991).

[14] D. F. Williams and R. B. Marks, Reciprocity Relations in Waveguide Junctions. Submitted to IEEE Trans. Microwave Theory Tech.

[15] D. F. Williams, R. B. Marks, D. K. Walker, and F. R. Clague, Wafer Probe Transducer Efficiency, IEEE Microwave Guided Wave Lett. 2, pp. 388–390 (1992).

[16] D. Williams, R. Marks, and K. R. Phillips, Translate LRL and LRM Calibrations, Microwaves & RF 30, 78 84 (1991).

[17] G. F. Engen and C. A. Hoer, Thru-Reflect-Line: An Improved Technique for Calibrating the Dual Six-Port Automatic Network Analyzer, IEEE Trans. Microwave Theory Tech. MTT-27, 987–993 (1979).

[18] R. B. Marks, A Multiline Method of Network Analyzer Calibration, IEEE Trans. Microwave Theory Tech. 39, 1205–1215 (1991).

[19] H.-J. Eul and B. Schiek, A Generalized Theory and New Calibration Procedures for Network Analyzer Self-Calibration, IEEE Trans. Microwave Theory Tech. 39, 724–731 (1991).

[20] M. Mrozowski and J. Mazur, Matrix Theory Approach to Complex Waves, IEEE Trans. Microwave Theory Tech. 40, 781–785 (1992).

About the authors: Roger B. Marks is a physicist and Dylan F. Williams a project leader in the Electromagnetic Fields Division of the Electronics and Electrical Engineering Laboratory, NIST, Boulder, CO. The National Institute of Standards and Technology is an agency of the Technology Administration, U.S. Department of Commerce.
