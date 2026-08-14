# Repair a satellite geolocation workflow

The supplied source is a historical slice of a remote-sensing package. A small
geostationary observation product and a cloud-top-height product can be read,
but the resulting geolocation is not physically consistent for supported
product inputs.

Run the offline reproduction, inspect the supplied scientific documentation,
and trace the product data flow. Repair the implementation so that the
documented satellite geolocation behavior holds for supported inputs. Keep the
workflow offline and preserve the package API used by the supplied runner.

Do not replace the workflow with a fixed report or a special case for the
public fixture. The implementation must work for other valid satellite
positions, cloud heights, masks, and target grids.
