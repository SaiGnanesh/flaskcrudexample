from basic import db,puppy


my_puppy=puppy('tony',5)

db.session.add(my_puppy)
db.session.commit()

#read

all_puppies=puppy.query.all()
print(all_puppies)

#select by id

puppy_one= puppy.query.get(1)
print(puppy_one)

#filers

puppy_frankie=puppy.query.filter_by(name='frankie')
print(puppy_frankie.all())


##update

first_puppy=puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()

##delete

second_pup= puppy.query.get(2)
db.session.delete(second_pup)

db.session.commit()

all_puppies=puppy.query.all()

print(all_puppies)
