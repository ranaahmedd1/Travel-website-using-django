from django.db import models

# Create your models here.
class Traveller(models.Model):
    #
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40,null=False)
    email=models.CharField(max_length=40,null=False)
    password=models.CharField(max_length=40,null=False)
    Confpassword=models.CharField(max_length=40,null=False,default='')
    favouritecities=models.CharField(max_length=40,null=True,blank=True)
    visitedCities=models.CharField(max_length=40,null=True,blank=True)

    def  __str__(self):
        return self.username
    # def newTraveller(self,email,confPaswrd):
    #     self.email=email
    #     self.confPaswrd=confPaswrd
    #     resultMSG=""
    #     all_users = Traveller.objects.all().filter(username=userLogin,password=passwrdLogin)
    #     if all_users : 
    #         return render(request, '',)
    #     # alreadyFound = cursor.fetchone()
    #     if alreadyFound :
    #         resultMSG="username Already exists" 
    #         # print
    #     elif not re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',self.email):
    #         resultMSG="Invalid Email"
    #     elif not re.match(r'^[a-z0-9_-]{3,15}$',self.username):
    #         resultMSG="choose proper username with only characters and numbers "
    #     elif self.paswrd != self.confPaswrd :
    #         resultMSG="Passwords don't match"
    #     elif not self.username or not self.paswrd or not self.confPaswrd or not self.email:
    #         resultMSG = "Please fill out the form !"
    #     else:
    #         cursor.execute('INSERT INTO `traveller`(`email`, `username`, `password`) VALUES ( % s, % s, % s) ',(self.email,self.username,self.paswrd) )
    #         mysql.connection.commit()
    #         resultMSG = 'You have successfully registered !'
    #     return render_template("signup.html",resultMSG=resultMSG)
   
