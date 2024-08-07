from setuptools import find_packages , setup 

requirements_file = "requirements.txt"
hyphen_e_dot = "-e ."

def get_requirements()->list[str]:
   with open (requirements_file) as requirement_file :
      requirement_list = requirement_file.readlines()
      requirement_list = [requirements_name.replace("\n" , "") for requirements_name in requirement_list]
      
   if hyphen_e_dot in requirement_list :
       requirement_list.remove(hyphen_e_dot)
   return requirement_list
     
    





setup (

    name = "sensor" , 
    version = "0.0.1" , 
    author= "iNeuron.ai" , 
    author_email="rajat.k.singh64@gmail.com" , 
    packages=  find_packages() , 
    install_requires = get_requirements() , 

)
