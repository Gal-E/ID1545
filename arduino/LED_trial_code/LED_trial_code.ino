
// Lets make our vibration example, using PWM!
#define LED_PIN 6

int i = 0;
int vibrState = 1;
int state = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600); // setting baud speed for Serial (a baud is a pulse)
  Serial.println("Lets start our pulsing vibration example!");
}

void loop() {

  // PWM takes values from 0 to 255, in our case, we want to make
  // a pulse effect, so we detect out of bounds behaviour and go to 127

  // incrementing the power of the vibration motor

  vibrationPattern();

  Serial.println(i);
  analogWrite(LED_PIN, i);
  delay(10); // in each step of pwm, we vibrate for i * 0.01 seconds

}

void vibrationPattern() {
  if (state == 0) {
    i = 0;
  } else if (state == 1) {
    i = 255;
  } else if (state == 2) {
    if (vibrState == 1) i += 10;
    if (vibrState == 2) i -= 10;

    if ( i > 255 && vibrState == 1) {
      vibrState = 2;
      i = 255;
    } else if (i < 0 && vibrState == 2) {
      vibrState = 1;
      i = 0;
    }
  }
}
