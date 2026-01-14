import yagmail
import pandas

sender = 'adarshsingh3002@gmail.com'
subject = "This is the subject"

# Use the 16-character App Password here, NOT your gmail login password
password = "rsxb foxq hvdv qzf" 
df=pandas.read_csv('contacts.csv')
print(df)
yag = yagmail.SMTP(user=sender, password=password)
try:
    for index,row in df.iterrows():
      contents = f"Here {row['name']} is the content"
      print(row['email'])
      yag.send(to=row['email'], subject=subject, contents=contents)
      print("Email Sent Successfully!") 
except Exception as e:
    print(f"Failed to send email. Error: {e}")