class ClassName:
    """Class docstring"""
    
    def __init__(self, parameters):#ทุกmethod ในclassต้องมีparamiter 
        # Constructor method
        self.attribute = value
    
    def method_name(self):
        # Instance method
        return something


myObj = ClassName(parameters)
print(myObj.attribute)
resultFromMethod = myObj.method_name()