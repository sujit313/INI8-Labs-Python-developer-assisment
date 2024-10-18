use assesment;

CREATE TABLE Registration (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100) NOT NULL,
  Email VARCHAR(255) NOT NULL UNIQUE,
  DateOfBirth DATE NOT NULL,
  Gender VARCHAR(10),
  Address TEXT,
  PhoneNumber VARCHAR(20),
  RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from Registration;