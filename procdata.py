from pyproj import Proj, Transformer, transform, CRS
from models import Incident, engine, Base, db_session

Base.metadata.create_all(bind=engine)
transformer = Transformer.from_proj(2868, 4326)

with open('Tucson_Police_Incidents__2019__Open_Data.csv') as f:
    lines = f.readlines()
    cnt = 0
    for l in lines:
        if cnt > 0:
            values = l.strip().split(',')
            city = values[15].strip()
            state = values[16].strip()
            zipcode = values[17].strip()
            desc = values[24].strip()
            x = float(values[-2].strip())
            y = float(values[-1].strip())            
            t = transformer.transform(x, y)
            latitude = t[0]
            longitude = t[1]
            # print([cnt, city, state, zipcode, desc, x, y, latitude, longitude])
            incident = Incident(description=desc, latitude=latitude, longitude=longitude)
            db_session.add(incident)
            db_session.commit()
        cnt += 1
