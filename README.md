ANDY
=======

Meet Andy, a multi-purpose humanoid robot built with a Raspberry Pi and a robosapien toy. Andy can walk, pick up and set down objects, take pictures, record video, and answer questions. Andy is voice controlled, so there is no need for a computer or smart phone to send him commands. Just say "Andy" wait for the beep, say your command, and Andy will do the rest.

Hardware
========

Andy is built out of inexpencive hardware, so no need for pocket loads of cash. A Robosapien is used for the body, making it easy to use and light in maintainance. A Raspberry Pi is the brain of Andy, making him a very intelligent machine. A cheap USB microphone is plugged into the Raspberry Pi's USB socket giving Andy ears. L298N and L293D motor drivers are used to control Andy's motors, and a MCP23017 chip is used to give the Raspberry Pi more General Purpose Input and Output ports (GPIO). Andy has vision with a Raspberry Pi SPI camera. With all of this powerful hardware, it makes a toy robot a very useful helper.

Software
========

Andy uses many different software packages to operate. Pocketsphinx is used for speech recognition, OpenCV is used for the vision, MySQL is used for Andy's database, and Python is used to combine everything together.

Commands
========

Cyclops can execute over 100 different seqences, But has ten keywords he responds to. To get Cyclops to respond to a command, first say "Cyclops" followed by the command. 

<h2>Cyclops, Walk</h2>

The first command is walk. After the walk command, you must tell Cyclops direction and distance. For example: "Cyclops walk forward 10 steps" will make cyclops walk forward ten steps. If you leave out the "steps" he will still walk forward ten steps. If you leave out the 10, Cyclops will walk forward until you give the stop command. The other direction commands are backward, left, and right.

<h2>Cyclops, What</h2>

"What" is a basic command. Using the what command, you can ask Cyclops basic questions like "Cyclops, what is you name?" or "Cyclops, what time is it?" or even "Cyclops, what is 5+13x43?" "What" commands are preprogrammed so you can't just ask Cyclops anything.

<h2>Cyclops, take</h2>
The "take" command is for the camera. There are two commands: "Cyclops, take picture", and "Cyclops take video". Take picture will just take a snapshot right from the current view. With take video, it will start the video and record.
