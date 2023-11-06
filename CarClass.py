class Car:
    def _int_(self, make, model, year)
        self.make = make
        self._model = model #protected attribute
        self.year = year
    
        #when we protect an attribute it's not accesible
        #outside of the class
        
        def get_model(self):
            return self._model