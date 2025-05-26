from sun_app import db

class Panel(db.Model):
    """
        Represents a solar panel in the database.
        Attributes:
            1.    id: Unique identifier for the panel.
            2.    name: Name of the panel.
            3.    manufacturer: Manufacturer of the panel.
            4.    length: Length of the panel in m.
            5.    width: Width of the panel in m.
            6.    area: Area of the panel in m2.
            7.    weight: Weight of the panel in kg.
            8.    density: Density of the panel in kg/m2.
            9.    price: Price of the panel in COP.
            10.   efficiency: Efficiency of the panel.
            11.   nominal_power: Nominal power of the panel in kWp.
            12.   open_circuit_voltage: Open circuit voltage of the panel in V.
            13.   short_circuit_current: Short circuit current of the panel in A.
            14.   mpp_voltage: Maximum power point voltage of the panel in V.
            15.   mpp_current: Maximum power point current of the panel in A.
            16.   voltage_temperature_coefficient: Voltage temperature coefficient of the panel in %V/°C.
            17.   current_temperature_coefficient: Current temperature coefficient of the panel in %A/°C.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    density = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=True) # Optional field for price
    efficiency = db.Column(db.Float, nullable=False)
    nominal_power = db.Column(db.Float, nullable=False)
    open_circuit_voltage = db.Column(db.Float, nullable=False)
    short_circuit_current = db.Column(db.Float, nullable=False)
    mpp_voltage = db.Column(db.Float, nullable=False)
    mpp_current = db.Column(db.Float, nullable=False)
    voltage_temperature_coefficient = db.Column(db.Float, nullable=False)
    
    @property
    def computed_area(self):
        return self.length * self.width
    
    
    @property
    def density(self):
        """
        Compute the density of the panel as weight divided by area.
        Returns:
            float: The density of the panel in kg/m2.
        """
        if self.area > 0:
            return self.weight / self.area
        return 0.0

    def __repr__(self):
        return f"<Panel {self.id}: {self.name} by {self.manufacturer}>"

    
class Inverter(db.Model):
    """
        Represents an inverter in the database.
        Attributes:
            1.    id: Unique identifier for the inverter.
            2.    name: Name of the inverter.
            3.    manufacturer: Manufacturer of the inverter.
            4.    nominal_power: Nominal power of the inverter in kWp.
            5.    no_mpp: Number of MPP inlets.
            6.    min_input_voltage: Minimum input voltage of the inverter in V.
            7.    max_input_voltage: Maximum input voltage of the inverter in V.
            8.    max_output_current: Maximum output current of the inverter in A.
            9.    output_voltage: Output voltage of the inverter in V.
            10.   weight: Weight of the inverter in kg.
            11.   width: Width of the inverter in m.
            12.   height: Height of the inverter in m.
            13.   depth: Depth of the inverter in m.
            14.   efficiency: Efficiency of the inverter.
            15.   price: Price of the inverter in COP.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    nominal_power = db.Column(db.Float, nullable=False)
    no_mpp = db.Column(db.Integer, nullable=False)
    min_input_voltage = db.Column(db.Float, nullable=False)
    max_input_voltage = db.Column(db.Float, nullable=False)
    max_output_current = db.Column(db.Float, nullable=False)
    output_voltage = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    depth = db.Column(db.Float, nullable=False)
    efficiency = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=True)  # Optional field for price
    
    def __repr__(self):
        return f"<Inverter {self.id}: {self.name} by {self.manufacturer}>"
    