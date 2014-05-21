#Database
#By Tyler Spadgenske

import mysql.connector

class Database():
        def __init__(self):
                self.conn = mysql.connector.connect(user='root', password='raspberry', database='ANDY')
                self.cursor = self.conn.cursor()
                self.objects = [None]
                self.scripts = [None]
                self.images = [None]
                self.color = None
                self.iceCream = None
                self.currentAge = None
                self.image = None
                self.seen = None
                self.bestie = None
                
        def get_object_data(self,target):
                query = ('SELECT id, object_name, script_path, image_path FROM objects')
                self.cursor.execute(query)

                for empid, object_name, image_path, file_path in self.cursor:
                        print empid, object_name, image_path, file_path
                        self.objects.append(str(object_name))
                        self.scripts.append(str(file_path))
                        self.images.append(str(image_path))

                self.num = 0
                for i in self.objects:
                        if i == target:
                                break
                        else:
                                self.num += 1
                                
                self.cursor.close()
                self.conn.close()

                return self.scripts[self.num], self.images[self.num]

        def get_people_data(self, target, data):
                #Get data from database
                query = ('SELECT id, first_name, favorite_color, favorite_ice_cream, age, image_path, last_seen, best_friend FROM people')
                self.cursor.execute(query)
                for id, first_name, favorite_color, favorite_ice_cream, age, image_path, last_seen, best_friend in self.cursor:

                        #Setup data
                        self.name = str(first_name)
                        if self.name == target:
                                self.color = str(favorite_color)
                                self.iceCream = str(favorite_ice_cream)
                                self.currentAge = str(age)
                                self.image = str(image_path)
                                self.seen = str(last_seen)
                                self.bestie = str(best_friend)

                #Return data wanted
                if data == 'first_name':
                        return self.name
                if data == 'favorite_color':
                        return self.color
                if data == 'favorite_ice_cream':
                        return self.iceCream
                if data == 'age':
                        return self.currentAge
                if data == 'image_path':
                        return self.image
                if data == 'last_seen':
                        return self.seen
                if data == 'best_friend':
                        return self.bestie
                else:
                        return 'Invalid Input'

                        
   
t = Database()
test = t.get_people_data('Tyler','favorite_color')
print test
