from main.models import Member, Exercise, BodyPart
from main.database import Session
from sqlalchemy import select, func, text

def listar_mimembros():
  session = Session()
  members = session.query(Member).all()
  for member in members:
    print(member)

def insertar_miembro():
  session = Session()
  nuevo_miembro = Member(
    name="Lucía Fernández",
    code="B102",
    dni="87654321",
    email="lucia@example.com",
    phone="555-6789"
  )
  # Agregar y confirmar la inserción en la base de datos
  session.add(nuevo_miembro)
  session.commit()
  print(nuevo_miembro.id)

def editar_miembro(member_id):
  session = Session()
  miembro = session.query(Member).filter_by(id=member_id).first()
  if miembro:
      # Actualizar campos específicos
      miembro.name = "Lucía Fernández Actualizado"
      miembro.email = "lucia_actualizado@example.com"
      miembro.phone = "555-9999"

      # Guardar los cambios
      session.commit()

      # Mostrar el registro actualizado
      print(f"Miembro actualizado: {miembro}")
  else:
      print(f"No se encontró ningún miembro con ID {member_id}")

def eliminar_miembro(member_id):
  session = Session()
  miembro = session.query(Member).filter_by(id=member_id).first()
  if miembro:
      session.delete(miembro)
      session.commit()
      # Mostrar el registro actualizado
      print(f"Miembro actualizado: {miembro}")
  else:
      print(f"No se encontró ningún miembro con ID {member_id}")

def query1():
  session = Session()
  ejercicios = session.query(Exercise).filter(Exercise.name.like('P%')).all()
  print(len(ejercicios))

def query2():
  session = Session()
  stmt = select(func.count(Exercise.id).label('cantidad')).where(Exercise.name.like('P%'))
  result = session.execute(stmt).scalar()
  print(result)
   
def query3():
  session = Session()
  resultados = session.query(Exercise, BodyPart).join(BodyPart).all()

  # Mostrar los resultados
  for ejercicio, parte_cuerpo in resultados:
      print(f"Ejercicio: {ejercicio.name}, Parte del Cuerpo: {parte_cuerpo.name}")

def query4():
  session = Session()
  sql = text("SELECT exercises.name, body_parts.name AS body_part FROM exercises JOIN body_parts ON exercises.body_part_id = body_parts.id")
  # Ejecutar la consulta
  result = session.execute(sql)

  # Mostrar los resultados
  for row in result:
      print(f"Ejercicio: {row[0]}, Parte del Cuerpo: {row[1]}")

query4()