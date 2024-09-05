class Electronics:
    class_info='I speak about Electronics Devices and the details are: '

    @classmethod
    def _class_info(cls):
        print(cls.class_info)

    def __init__(self,name,type,year,prize) -> None:
        self.device_Name=name
        self.device_type=type
        self.device_manf_year=year
        self.device_avg_prize=prize

    def __str__(self) -> str:  #represent what need to be returned when the object is referenced.
        return f'Device name: {self.device_Name}'
    
    def _get_details(self):
        print(f'Device_Name: {self.device_Name}')
        print(f'Device_Type: {self.device_type}')
        print(f'Device_Manufactured_Year: {self.device_manf_year}')
        print(f'Average_Device_Prize: {self.device_avg_prize}')

Mobile=Electronics('One_plus','AndroiD_Mobile',2016,'30,000')
Mobile._class_info()
Mobile._get_details()