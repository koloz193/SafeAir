int button, button_state;

void setup()
{
  button = 8;
  button_state = 0;
}

void loop()
{
  button_state = digitalRead(button);

  if (button_state == HIGH)
  {
    system("python ~/gas_detect.py");
  }
}
