<style>
html {
  scroll-behavior: smooth;
 }
#main_content{
  max-width: 900px;
  }
#main_content_wrap {
  background: white;
  }
#header_wrap {
  background-image: url("images/background.png");
  background-repeat: no-repeat;
  background-size: 100% 100%;
  }
#project_tagline, #project_title {
  text-shadow: none;
  font-family: monospace;
  }
#main_content_wrap {
  border: none;
  }
#second-header {
  margin-bottom: 60px;
  border-bottom: 1px solid #34A853;
  padding: 10px 0 40px 0;
}  
#second-header a {
    color: #34A853;
    font-family: monospace;
    font-size: 18px;
    margin: 0 4%;
 }
 #second-header a:hover {
    text-decoration: none;
    color: #FBBC05;
    font-weight: 700;
 }
.headline {
    font-family: monospace;
    color: #4285F4;
    text-align: center;
    margin-bottom: 25px;
    font-size: 26px;
  }
  .highlight {
    border-bottom: 6px #FBBC05 solid
  }
  h4 {
    font-size: 20px;
    font-family: monospace;
    text-align: center;
    color: #FBBC05;
  }
  h4.secondary{
    text-align: left;
    color: #34A853;
  }
  .brainstorm_idea {
    width: 40%;
    float: left;
    margin: 20px;
    height: 550px;
    box-shadow: 2px 2px 5px grey;
    padding: 16px;
    border-radius: 10px;
  }
  .brainstorm_idea:last-child {
    width: 88%;
    height: 300px;
    margin-bottom: 60px;
  }
  div img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: none;
    box-shadow: none;
   }
  b{
    font-weight: 700;
  }
  .description {
    text-align: center;
  }
  #theidea{
      display: inline-block;
  }
  h5 {
    font-family: monospace;
    font-weight: 600;
    font-style: italic;
    font-size: 21px;
  }
  video.firstVideo {
    width: 39%;
    margin: 0;
    display: inline;
  }
  img.half {
    width: 50%;
    margin-bottom: 0px;
    display: inline;
    float: right;
  }
  video.protoVideo {
    width: 100%;
  }
  span.textNearImg {
    display: inline-block;
    width: 100%;
    margin-top: 20px;
 }

  #BreadboardImage {
    float: right;
    width: 30%;
    margin: 0 0 10px 30px;
  }
  #myBtn {
    display: none;
    position: fixed;
    bottom: 40px;
    right: 50px;
    z-index: 99;
    border: none;
    outline: none;
    background-color: #34A853;
    cursor: pointer;
    padding: 15px;
    border-radius: 4px;
    background-image: url("images/arrow-up.png");
    background-repeat: no-repeat;
    background-size: 50%;
    background-position: center;
    width: 50px;
    height: 50px;
  }

  #myBtn:hover {
    background-color: #555;
  }
  #briefEx {
    padding: 0 200px;
  }
</style>
<script>

var mybutton = document.getElementById("myBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
var mybutton = document.getElementById("myBtn");

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
</script>

<button onclick="topFunction()" id="myBtn" title="Go to top"></button>

<div id="second-header">
  <a href="#brainstorm">Brief Brainstorm</a>
  <a href="#theidea">The Concept</a>
  <a href="#process">The Process</a>
  <a href="#prototype">The Prototype</a>
</div>

<div id="brainstorm">
  <h3 id="briefEx" class="headline">Enhancing the connection between a human and a smart device</h3>
  <div class="description">
    At the start off this course we received the design brief to add value to a wheelchair by designing and prototyping an IoT solution. We began by investigating the challenges and opportunities that currently exist in wheel chair use, so we could understand what could be gained by creating a connected wheel chair. 
    Through online research and interviews with two [hysiotherapists and an occupational therapist student that volenteers with wheelchair users, we increased our understanding of the problem scenario and came to the following design challenge:
    <br><br>
   <h5> "While the population of wheelchair users is growing worldwide, it becomes urgent to design supportive
technologies that fit their needs. We aim to develop products for improvement of the wheelchair users’ wellbeing. This design is a connected product that collects
data from sensors, processes it in order to actuate user
interactions embedded on the wheelchair."</h5>
    <br><br>
    
  We started our design process by creating an overview of our initial associations and the potential sensors and actuators that we could come up with. We used this overview to gather potential applications and map our primary associations. This session helped us form several ideas for a connected wheelchair:
  </div><br><br>

  <div class="brainstorm_idea">
  <h4>Being Superheros</h4>
  <br>
  Research has shown that while using a wheelchair, items are often out of reach or misplaced. Some might be placed too high for a wheel chair user, like for example a mirror in the bathroom, or the heater button.
  <br><br>
  With the growing interest in building smart houses, we envisioned a house where objects could move to adjust themselves to the wheelchair user. Examples hereof could be doors that open automaticly, a mirror that could change it's angle to the right position and the heating could turn on.
  <br><br>
<b>System:</b> Chair > Object in Physical world (an App interface to control preferences)<br>
<b>Optional Sensors:</b> Movement, Voice control, GPS, Touch, Gyroscope <br>
<b>Optional Actuators:</b> Speakers, LEDs, vibration

  </div>

  <div class="brainstorm_idea">
   <h4>Getting Around</h4>
    <br>
    Can we help people to get around more easily?
    <br>
    We realized that "Google maps" could in some scenarios not suffice for wheelchair users. Instead, we deemed it potentially valuable to suggest routes considering their limitations and provide them with the optimal traveladvice. This could be helpful in different environments such as hospitals, big buildings like the TU or other universities, or in general in the city.
<br><br>
<b>System:</b> App > Chair > Physical world > App<br>
<b>Optional Sensors:</b> Touch, Acceleration, GPS, Compass, Distance, Movement<br>
  <b>Optional Actuators:</b> Speakers, LEDs, vibration, screen

  </div>

  <div class="brainstorm_idea">
    <h4>Increasing Safety</h4>
    <br>
    Can we make it safer to use a wheelchair on the go?
    <br>
    Insired by different insurance and driving apps, we also envisioned an app that actively monitors ground quality, to signal the user to drive more carefully on potentially unstable ground. In addition to that, this app could report selected contacts about possible dangours or accidents to increase safety and independence for the wheelchair user. By applying accident detection, a panic button, collision detection and more, we would hope to make the wheelchair experience as safe as possible
    <br><br>
  <b>System:</b> Physical world > Chair > App<br>
  <b>Optional Sensors:</b> Touch, Gyroscope, Acceleration, GPS, Distance, temperature, Movement, voice<br>
  <b>Optional Actuators:</b> Speakers, LEDs, vibration, screen

  </div>

  <div class="brainstorm_idea">
    <h4>Be Active</h4>
    <br>
    How can we help wheelchair users to enjoy physical activity more?
    <br>
    Inspired by various fitness apps, we envisioned a product that would enable wheelchair users to become more active and spend more time outside. The app would connect to the chair and collect different fitness data such as amount of force put on the wheels, kilometers driven, road incline, meters climbed, etc.
  <br><br>
  <b>System:</b> Physical world > Chair > App<br>
  <b>Optional Sensors:</b> Gyroscope, Acceleration, GPS, Distance<br>
  <b>Optional Actuators:</b> Speakers, LEDs, vibration, screen
  </div>

  <div class="brainstorm_idea">
    <h4>Gamify It</h4>
    <br>
    Focusing mostly on kids, or people who are in the wheelchairs for short-term revalidation in hospitals, we were inspired by Pokemon Go to consider a connected wheelchair that empowers users to overcome obstacles, find the best routes and using the chair to play games with other wheelchair users. This would serve helping users get better at using their chair.
    <br><br>
  <b>System:</b> App > Chair > Physical world  > App<br>
  <b>Optional Sensors:</b> Touch, Voice control, GPS, Compass, Distance, Movement<br>
  <b>Optional Actuators:</b> Speakers, LEDs, vibration, screen
  </div>
</div>

<div id="theidea">
  <h3 class="headline">The Final Concept: <br>Basic wheelchair skills gamification</h3>
  <span>For our final conecpt, we chose to focus on the first experience of a user with a wheelchair. We designed
   a connected wheelchair that helps teach basic wheelchair skills. Since being confined to this chair can be quite impactful and in worst case scenario lifechanging, we wanted to help these children to get used to this extension of their body in a fun way. Our goal with this prototype is to use the connected prototype in order to test it with kids and perform user research. </span>
  <span class="highlight"> We want to test the posibility of gamifying the first time use of a wheelchair, in order to simplify and shorten the learning curve of basic wheel chair skills.</span>
  <br><br>
  <h4 class="secondary">Target Users:</h4>
 <ul>
   <li>Main target: Kids in the age of 6-12</li>
  <li>Secondary users: Temporary users in hospital or first timers</li>
  <li>Anyone interested in learning basic wheelchair skills</li>
  </ul>

 <img src="images/Child in a wheelchair 2.jpg" style="border: none;box-shadow: none; margin-bottom: 25px;"/>
        <br>
  <h4 class="secondary">Goals:</h4>
The goal of the product is to teach kids basic wheelchair activities in a fun and playful manner. A secondary goal is to use the data collected to learn more about how kids adapt to using wheelchairs, the speed at which they learn and the level of difficulty of different activities. <span class="highlight">The goal of this prototype is to test the usability of both the web interface, and the physical product and experience. Our aim is to learn whether this product can create value for its target audience and whether it can make the learning process more enjoyable.</span>
<br><br>

<ul>
  <li>Gamify simple tasks that involve wheelchair skills</li>
<li>Encourage kids in wheelchairs to be active and play outside</li>
<li>Create a community</li>
<li>Teach basic wheelchair skills</li>
<li>Learn about wheelchair first timers</li>
</ul>

<h4 class="secondary">Architecture</h4>

<div>
The user will receive a task from an app, which he will execute with the wheelchair. The app would indicate how well the task was performed and will enable the user to try again or try a different task

<div>
  <img src="images/img1.png" class="img1"/>
</div>

A possible example of a task would be: “Drive a full circle to your right!”. The task would have a timer counting the time it took the user to complete the circle. A visual on the screen will indicate to the user the progress in percentages. After the task is complete the user will receive starts to indicate how well he performed the task based on time. 1 star would indicate basic skills and 3 starts would indicate professional skills. At completion, a sound and action on the visual will indicated how well the user performed. The task can become more difficult over time by doing the same thing while going uphill or on a different surface such as grass or sand.</div>

<div style="margin: 0 auto;text-align: center;">
  <img src="images/img2.png" style="width: 60%;border: none;box-shadow: none;"/>
</div>



</div>
<ul>
<li>System: App > User > Physical world > Wheelchair > App</li>
<li>Optional Sensors: Movement, Acceleration, Touch, Measure the angle</li>
<li>Optional Actuators: Speakers, LEDs, vibration</li>
 </ul>

<div>
  <img src="images/Architecture.png" style="border: none;box-shadow: none; margin-bottom: 25px;"/>
</div>

<h4 class="secondary">Data:</h4>
<b>Data collected:</b><br><br>
Speed on different surfaces, angles, time it taked to perform various activities such as complete a circle, reverse etc<br><br>
<b>The data collected can teach us about: </b>
<ul>
  <li>The behaviour of kids when they use a wheelchair for the first time</li>
  <li>What skills are more challenging for kids to learn when using a wheelchair for the first time</li>
  <li>The time it takes to perform different activities with a wheelchair</li>
  <li>The learning curve of different skills, and how can we improve it</li>
  </ul>
<b>Possible stakeholders:</b><br>
<ul>
  <li>Wheelchairs engineers and designers </li>
  <li>Doctors</li>
  <li>Physiotherapists</li>
  <li>Occupational therapists</li>
  <li>Families of kids with wheelchair</li>
  <li>Researchers </li>
 </ul>


<h3 id="process" class="headline">The process</h3>
<p> Within this project, the responsibility for the development of different parts was divided within the group. Gal mainly worked on developing the front end; the web-interface and the user interface. Niels worked on implementing the electronics on the wheelchair and the back-end; the Arduino and Python code. In the following steps, we'll describe how our project can easily be reproduced.</p>
  <div>
    <h4 class="secondary">1. Create a new Github project</h4>
     <p>For managing our collaborative work on this digital project we used an organizational GitHub account, which allowed us to store different versions of our codes and work from different pc's on the same files. An additional added value of using GitHub is that within its interface, an option is built in that allows one to quickly convert code documents into a presentable website. Be careful to create an organizational account instead of a normal user account; you will need the account to be organizational in order to be able to grant everybody administrative permission, so that all your teammembers can edit the GitHub pages if necessary. </p>
    <h4 class="secondary">2. Set-up the Raspberry Pi</h4>
      <p>The Raspberry Pi (Pi from now) serves as the most important node within our project, collecting the data from the Adafruit bluetooth board, doing calculations on the raw data in a python file and then displaying this data on the server it is running. <br> We started working with a clean install of Raspbian. To be able to work with the Pi, beware that you will need a keyboard, a mouse and a screen with HDMI gate. First, the Pi had to be set up to recognize the Eduroam network. Then, through the terminal on the Pi, download a copy of the GitHub project folder. For more indepth instructions, please refer to <a href="https://datacentricdesign.org/docs/2019/04/30/platform-raspberrypi">this tutorial</a>. </p>
  <h4 class="secondary">3. Build the Adafruit breadboard</h4>
  <div id="BreadboardImage">
  <img src="images/Breadboard Adafruit.png" style="border: none;box-shadow: none; width: 100%;"/>
</div>
      <p>The core sensor to our project was the BNO055 IMU sensor; this is a 9 axes accelerometer that can detect movement, rotation and accelerations. For now, we're only referring to one axis: the vertical rotation. This IMU sensor is connected to the Adafruit Sensor according to the schematic that can be seen below:</p>
        <ul>
          <li>3V on Adafruit to Vin on IMU - power supply for the IMU sensor</li>
          <li>SDA on IMU to SDA on Adafruit - dataline to communicate measured data</li>
          <li>SCL on IMU to SCL on Adafruit - clockline to synchronise the communicated data</li>
          <li>GND on IMU to GND on Adafruit - grounding the IMU sensor</li>
        </ul>

<div id ="How to build it continued">
    <h4 class="secondary">4. Download Arduino and install libraries</h4>
  <p>In order to be able to work with the Adafruit, we need to do some quick setup. First of all, one is required to install <a href="https://www.arduino.cc/">the Arduino software</a> and install the following libraries within the Arduino code, by going to Sketch -> Include Library -> Manage Libraries:</p>
        <ul>
          <li>Bluefruit nRF51</li>
          <li>Adafruit Unified Sensor</li>
        </ul>
  <p>Then, go to 'preferences' and next to the field "Additional Boards Manager URLs:" click on the button with two overlapping rectangles, all the way to the right. Copy-paste “https://adafruit.github.io/arduino-board-index/package_adafruit_index.json" into this window, then click 'OK' in this screen and in the 'Preferences' window. </p>
    <h4 class="secondary">5. Upload arduino code to Adafruit</h4>
  <p>Now connect the Adafruit board to your PC using an micro-usb cable. In the topbar of the Arduino software, go to 'tools' and make sure that 'board' is set to "Adafruit 32u4" and that, under 'port' a usb-port is selected with "Adafruit 32u4" in the name, as well. Download the following <a href="https://github.com/Gal-E/ID1545/tree/master/arduino/IMU_detector">arduino file</a> and open it in the arduino software. Please make sure that you download both the "IMU_detector.ino" and the "BluefruitConfig.h" file and store them in the same folder, otherwise the arduino software won't have access to certain crucial functions in the "IMU_detector.ino" file. Push the arrow in the top bar of the Arduino interface to upload the file to the Adafruit board. Now, when connected to power, the Adafruit should be visible by bluetooth devices.</p>
    <h4 class="secondary">6. Set-up Python file on Pi for subscribe_gatt_orientation.py</h4>
  <p>Next, we'll set up the Pi to be able to collect the IMU data, calculate the progress made and display that on the server. Download the <a href="https://github.com/Gal-E/ID1545/blob/master/requirements.txt">'requirements.txt'</a> file and install it. You can do this by first going to the Git directory on your pc using the 'cd + [name_of_directory]'-command in your terminal and then running 'pip3 install -r requirements.txt --user'. Next, create a 'py' folder in the Git directory on the Pi. Download <a href="https://github.com/Gal-E/ID1545/blob/master/py/subscribe_gatt_orientation.py">subscribe_gatt_orientation.py</a> in this folder. Also download <a href="https://github.com/Gal-E/ID1545/blob/master/py/complete.wav">complete.wav</a> into the 'py' folder on your Pi, so that we can let the user hear a celebratory sound when they have completed their assignment*. For a more intricate explanation of what this code does and how it works, please read the comments in this file itself.<br><br>*Copyright of this sound fully goes to Duolingo, and is merely used here as an educative example.</p> 
    <h4 class="secondary">7. Write html code, download javascript code for interface</h4>
    <p>To create a web interface for the prototype, we decided to use an existing JS library and adjust it to our needs. We wanted to create a circle to indicate the movement that occurs in the physical world with the chair. We tried different libraries until we chose the one that suited our needs most. At first we used a loader JS library. It looked great but we realized that making it work for left and right circles we would have to re-write quite a lot of the code. We decided to try a different library and chose to use a pie chart. That way, both sides of the circle are supported. The html code takes the values -100 to 100 from the SGO files and translates this to a certain percentage of how far along you are in making a circle.</p>
    <h4 class="secondary">8. Run python script on Raspberry Pi</h4>
<p>Now, in the terminal on the Pi (or from your PC when you are connected to the Pi), type 'hostname -I' to reveil the IP-address of the Raspberry Pi. Write this down somewhere. Next, 'cd' to the Git directory, type 'python3 py/subscribe_gatt_orientation.py' and press enter. The code should start running. If it complains about any libraries that it doesn't recognise, simply run 'pip3 install [name of library]' until it doesn't come across unknown libraries anymore. With the Adafruit breadboard connected to power, the blue indicator LED on the Adafruit should light up in confirmation that a bluetooth connection between the Adafruit and the Pi has been established. Now, the server should be live as well. Using the IP address we retrieved just now, go to "http://145.94.XXX.XXX:5000/donut". This should show you the web-interface we referred to in the previous step, with a progress bar that shows you how far along you are in making a circle.</p>
<div id="prototype"></div>
<h3 class="headline">The prototype</h3>
<p>While developing the prototype we faced many considerations: What would be the best place on the chair to attach the board? What type of angle should we monitor in order to test a full circle? What should happen when a circle is complete? etc. The ability to physically test the different options helped us make the right decisions.</p>
<br><br>

 <div>
    <video controls autoplay muted class="firstVideo">
        <source src="images/video.mp4" type="video/mp4">
    </video>
    <img class="half" src="images/img6.png" style="border: none;box-shadow: none;"/>
</div><br><br>
<h5 style="text-align: center;">The Final Prototype</h5>
<p>
The final prototype consists of a web interface that demonstrates the circle done with the wheelchair. As the chair rotates, the circle in the web application gets fuller, thus indicating the percents of the circle that have been complete. Once the circle is complete, there is a confetti animation and a success sound, letting the user know he completed the exercise. This can be seen in the video bellow. The first video records the activity on the screen. 
</p><br><br>

  <video controls autoplay muted class="protoVideo" style="width: 35%;float: left;">
      <source src="images/video5.mp4" type="video/mp4">
  </video>
  <video controls autoplay muted class="protoVideo" style="width: 64%;float: right;">
      <source src="images/video8.mp4" type="video/mp4">
  </video>
    <br>

  <div>
     <span class="textNearImg">In the console log you can see how we track every angle, and the visual on the screen changes to reflect that to the user (The numbers 0 - 100 indicate angle 0 untill angle 360). In the second video, you can see how the prototype is being used, while the web app appears on the users phone.</span>
  
 </div><br>
   <video controls autoplay muted class="protoVideo">
      <source src="images/video2.mov" type="video/mp4">
  </video>
  <br>
  <p>For any further questions related to reproducing this project, please contact n.j.a.weggeman@student.tudelft.nl. Thanks for reading!!</p>

