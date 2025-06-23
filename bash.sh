#!/bin/bash

echo "Enter your username:"
read username

echo "Enter your password:"
read password

if [ $username == "Rofa" ] && [ $password == "1234" ]; 
then
  echo "Login successful"
else
  echo "Incorrect"
fi