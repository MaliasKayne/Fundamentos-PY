## modules ##
#definition
import mymodule
from mymodule import generate_full_name as fullname
print(mymodule.generate_full_name('Jossie', 'Diaz'))
#print(generate_full_name('Alexandra', 'Rodrigez'))
print(fullname('Alexandra', 'Rodrigez'))