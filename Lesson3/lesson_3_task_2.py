from smartphone import Smartphone

catalog = []

phone1 = Smartphone('honor', '90 12GB+512GB', '+79108737214')
phone2 = Smartphone('techo', '20C 4/128GB', '+79101280499')
phone3 = Smartphone('poco', 'x6 pro', '+79104589629')
phone4 = Smartphone('huawei', 'nova 11', '+79103435698')
phone5 = Smartphone('realme', 'C514/128 GB', '+79101235897')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")