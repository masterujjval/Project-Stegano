# Project-Stegano

## About

<strong> Project-Stagno</strong> is the CLI tool made under the guidance of IBM-Skillbuild and Edunet mentors. <strong> Project-Stagno</strong> is the final project for completing the internship of Edunet with IBM-Skillbuild.

The project is based on the steganography techniques to encrypt the message and an individual with the symmetric key will be able to decrypt the message.

<strong>Project-Stegano</strong> have two options:
- Hide text in the image
- Hide messages using AES encryption

## Installation of the tool

### Linux

- Clone the repository to your node
- provide the required permission to run the bash script, run the command ``` sudo chmod +x *```
- run ```./run-tool```

```run-tool``` will install all the required files and execute the script after installing all the dependencies 

### Windows
***NOTE:*** execute the command ```pip3 install -r requirements.txt``` to install the dependencies.
For Windows, there are two ways to run the script in CLI:
- Using python3
  - Execute ```python3 main.py``` for <strong>Text in Image Encryption</strong>
  - Execute ```python3 encrypt-msg.py``` for <strong>Text encryption</strong>

- Using git bash/WSL(ubuntu from Microsoft)
  - follow the same Linux commands mentioned above

## Sample and test case

### Text Encryption

- Enter an option to encrypt or decrypt the plain/cipher text.

  - ![Screenshot from 2023-11-11 00-54-10](https://github.com/masterujjval/Project-Stegano/assets/64778409/40b11d0e-657f-4ccd-9fc8-dae6e47b1c07)

- Copy the text and key displayed after a single quote (' ')

  - ![Screenshot from 2023-11-11 00-56-50](https://github.com/masterujjval/Project-Stegano/assets/64778409/2ab6da37-cdce-4cbb-b20f-85096329dddc)


- To decrypt the cipher text choose option 2
  - ![Screenshot from 2023-11-11 01-01-54](https://github.com/masterujjval/Project-Stegano/assets/64778409/0079c774-984f-4a3b-ad75-d97e9d76d73f)

## Text Hiding in an Image

***It is recommended to store the image in the same folder of the cloned repository.***

![Screenshot from 2023-11-11 01-07-14](https://github.com/masterujjval/Project-Stegano/assets/64778409/411a6c31-7325-4c15-a721-80d58654fd6d)

Type the image name or path to the image (.jpg or jpeg) and then enter the password. A new image will be generated with hidden text. The password will be the symmetric key and should shared with caution if an individual wants to get the text from the image, a symmetric key would required.

![Screenshot from 2023-11-11 01-09-07](https://github.com/masterujjval/Project-Stegano/assets/64778409/174efcb2-0d71-4e6f-9628-6be8b9027193)

Decoding the text from the image is the same just choose the decode option and viola!!

![Screenshot from 2023-11-11 01-15-46](https://github.com/masterujjval/Project-Stegano/assets/64778409/82c5236d-4217-47b9-b071-a88f562167f1)














