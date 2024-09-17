
# Word Blocks
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc0af021259cf2b86/6021b32552af9c14d9058343/word-blocks.png)
## Block Descriptions

### Motor Blocks Category
Motor Blocks either make the motors run or get information from the motors. The *Motor Blocks* category contains the most common Motor Blocks.
#### Run Motor for Duration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt8a1e5707faadcee9/610bb40376f3370f3d3dec4f/gecko_block_help_flippermotor_motorturnfordirection_en.svg)

This block will run one or more motors clockwise or counterclockwise for a specified number of rotations, seconds, or degrees. 

The motor speed is set by the Set Speed Block. The default speed is 75%.
#### Motor Go to Position
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt496978a465d9d814/610bb3c6a371cc66abf8d46b/gecko_block_help_flippermotor_motorgodirectiontoposition_en.svg)

This block sets one or more motors to a speciﬁed position. The motor can be set to run clockwise, counterclockwise, or to take the shortest path to the specified position. The position ranges from 0 to 359 degrees.  <br><br>The motor speed is set by the Set Speed Block. The default speed is 75%.
#### Start Motor
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte108f2603d05a998/610bb38be47fc947da5ad344/gecko_block_help_flippermotor_motorstartdirection_en.svg)

This block will run one or more motors clockwise or counterclockwise forever. The motor speed is set by the Set Speed Block. The default speed is 75%.
#### Stop Motor
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt39f0fc5bfc0d107b/610bb3523b72a64d5a5a66f9/gecko_block_help_flippermotor_motorstop_en.svg)

This block stops one or more motors from running. The motor will brake so that it quickly comes to a complete stop.
#### Set Motor Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4b0dbb41b4f07d51/610bb31ee47fc947da5ad328/gecko_block_help_flippermotor_motorsetspeed_en.svg)

This block sets the speed of one or more motors. The speed range is -100 to 100. Negative values will reverse the direction of the motor. If the speed hasn't been specified, the default value is 75%.
#### Motor Position
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2a52ceb019e45719/610bb2ec62e91256b88bd7b5/gecko_block_help_flippermotor_absoluteposition_en.svg)

This block reports the current position of a motor. The position is given in degrees from 0 to 359.
#### Motor Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blta48b219a3c29e511/610bb2bcea63a36cfecbf80e/gecko_block_help_flippermotor_speed_en.svg)

This block reports the current speed of a motor. The value given is the motor's actual speed, not the speed set by the Set Speed Block.
### Movement Blocks
Movement Blocks enable you to run two motors in a synchronized motion. They're primarily used to move Driving Bases around. Only motors of the same type (e.g., two Medium Motors) can be synchronized.
#### Move for Duration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3f704f439d0ec66e/610bad46ae56136e76cf08bf/gecko_block_help_flippermove_move_en.svg)

This block moves a Driving Base either forward or backward for a specified number of centimeters, inches, seconds, degrees, or rotations. The distance that's moved in centimeters and inches depends on how the Driving Base has been built. Use the <i>Set 1 Motor Rotation to Distance Moved</i> Block to calibrate your Driving Base.
#### Start Moving
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd71f490590631b79/610bad14e04540748db7b7fc/gecko_block_help_flippermove_startmove_en.svg)

This block starts moving a Driving Base either forward or backward.
#### Move with Steering for Duration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc3f214652af56975/63602ccb26b2ae45c71ba9fa/gecko_block_help_flippermove_steer_en.svg)

This block moves a Driving Base forward for a certain duration with the possibility of steering. Higher steering values (i.e., +99 and -99) will make the arc path of the Driving Base sharper. Use a value of “0” to drive in a straight line. Using the values 100 and -100 will make the Driving Base pivot on itself.
#### Start Moving with Steering
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2565c100663b2f33/63602cd12d80d114d5ee5a37/gecko_block_help_flippermove_startsteer_en.svg)

This block starts moving a Driving Base forward with the possibility of steering forever. Higher steering values (i.e., +99 and -99) will make the arc path of the Driving Base sharper. Use a value of “0” to drive in a straight line. Using the values 100 and -100 will make the Driving Base pivot on itself.
#### Stop Moving
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd9d665c728e3cd86/610bac7fe4c07e100f460b69/gecko_block_help_flippermove_stopmove_en.svg)

This block stops all movement of a Driving Base by braking the motors.
#### Set Movement Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2c8b04f2715d4fd9/610bac4d9d8a044542c481f4/gecko_block_help_flippermove_movementspeed_en.svg)

This block sets the speed of a moving Driving Base. The speed range is -100 to 100. Negative values change the direction of the movement. The default value is 50%.
#### Set Movement Motors
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt942a4831d10e9cb5/610bac1c62e91256b88bd6b7/gecko_block_help_flippermove_setmovementpair_en.svg)

This block defines the Ports to which the 2 driving motors are connected.
#### Set 1 Motor Rotation to Distance Moved
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt75f86c02593ad2c5/610babeaa998331096737cd4/gecko_block_help_flippermove_setdistance_en.svg)

This block calibrates the distance of a Driving Base so that the  distance unit (i.e., centimeters/inches) specified in the Movement Blocks will be accurate.
### Light Blocks Category
Light Blocks enable you to turn the lights of different elements (e.g., 5x5 Light Matrix of the Hub, Distance Sensor lights) on and off.
#### Turn On 5x5 Light Matrix for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf273e7fb4ef7331b/638efd16b7ca873a85da30fd/gecko_block_help_flipperlight_lightdisplayimageonfortime_en.svg)

This block creates a pattern and makes it light up on the 5x5 light matrix for a specified length of time. The Block will turn the pixels off when the time is up.
#### Turn On 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltcda55de7fb392797/6356ee58590d796e630cccc9/gecko_block_help_flipperlight_lightdisplayimageon_en.svg)

This block creates a pattern and makes it light up on the 5x5 light matrix. The pattern stays lit up until the light matrix is told to do something else or the program is stopped.
#### Write on 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6609e4d9e9620456/638e4c56d745a637d78f7949/gecko_block_help_flipperlight_lightdisplaytext_en.svg)

This block displays a text string on the 5x5 light matrix by scrolling one letter at a time over the display.

#### Turn off 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc71b4a6ade9c8c6a/638f163ffca92b14440f07ac/gecko_block_help_flipperdisplay_lightdisplayoff_en.svg)

This block turns off all the lights on the 5x5 light matrix.
#### Set 5x5 Light Matrix Brightness
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt489463007ff9af8d/638efebd499626301e44801c/gecko_block_help_flipperlight_lightdisplaysetbrightness_en.svg)

This block sets the brightness of the 5x5 light matrix for the next block in the programming stack that will use the light matrix, such as the Turn On 5x5 Matrix Block. If the brightness has not been specified, the default value is 100%.
#### Set Pixel Brightness on 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb16dea2108faa053/638efe788424692b161e73bf/gecko_block_help_flipperlight_lightdisplaysetpixel_en.svg)

This block sets the brightness of an individual pixel on the 5x5 light matrix. Only the specified pixel is updated. The rest of the light matrix remains unchanged.
#### Rotate Orientation of 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt907dda9b1bb3b309/638efec9a86c73145ab709c7/gecko_block_help_flipperlight_lightdisplayrotate_en.svg)

This block rotates the orientation of what's being shown on the 5x5 Light Matrix either clockwise or counterclockwise.
#### Set Orientation of 5x5 Light Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt74376b6fe29f73a7/638f1238ea002a2c92dcaedc/gecko_block_help_flipperlight_lightdisplaysetorientation_en.svg)

This block sets the orientation of what's being shown on the 5x5 light matrix. The orientation can be set to <i>upright</i>, <i>upside down</i>, <i>left</i>, or <i>right</i>. The default orientation is <i>upright</i>.
#### Turn On 3x3 Color Matrix for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf99abc1b7dd6b66f/638e3ddc6c57a720091b7b1b/gecko_block_help_flipperlight_lightcolormatriximageonfortime_en.svg)

This block creates a pattern and makes it light up on the 3x3 color matrix for a specified length of time. The Block will turn the pixels off when the time is up.
#### Turn On 3x3 Color Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2210e7655084119e/638e3c321523f839d45769c3/gecko_block_help_flipperlight_lightcolormatriximageon_en.svg)

This block creates a pattern and makes it light up on the 3x3 color matrix. The pattern stays lit up until the light matrix is told to do something else or the program is stopped.
#### Turn off 3x3 Color Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt0627dd9ff32b1b48/638e41bb6645c8286cf72fbc/gecko_block_help_flipperlight_lightcolormatrixoff_en.svg)

This block turns off all the lights on the 3x3 color matrix.

#### Set 3x3 Color Matrix Brightness
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt831556f80af76b21/638e425bf987a41470cdf344/gecko_block_help_flipperlight_lightcolormatrixsetbrightness_en.svg)

This block sets the brightness of the 3x3 color matrix for the next block in the programming stack that will use the color matrix, such as the Turn On 3x3 Color Matrix Block. If the brightness has not been specified, the default value is 100%.
#### Set Pixel Brightness on 3x3 Color Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb01341cef5d233b9/638e4b893bf0dc23e14ad2bf/gecko_block_help_flipperlight_lightcolormatrixsetpixel_en.svg)

This block sets the color and brightness of an individual pixel on the 3x3 color matrix. Only the specified pixel is updated. The rest of the color matrix remains unchanged.
#### Rotate Orientation of 3x3 Color Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltcef38418452570a8/638e423443a2f0343d04c2b6/gecko_block_help_flipperlight_lightcolormatrixrotate_en.svg)

This block rotates the orientation of what's being shown on the 3x3 Color Matrix either clockwise or counterclockwise.
#### Set Orientation of 3x3 Color Matrix
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb82b57ccd571bd12/638721633f69f65d486d1050/gecko_block_help_flipperlight_lightcolormatrixsetorientation_en.svg)

This block sets the orientation of what's being shown on the 3x3 color matrix. The orientation can be set to <i>upright</i>, <i>upside down</i>, <i>left</i>, or <i>right</i>. The default orientation is <i>upright</i>.
#### Set Center Button Light
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6976e213671265d3/638a01179d315035d0d31f9f/gecko_block_help_flipperlight_centerbuttonlight_en.svg)

This block sets the color of the Center Button light.
#### Light up Distance Sensor
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4435b2a565155716/632083b003900149199aea19/gecko_block_help_flipperlight_ultrasoniclightup_en.svg)

This block turns the Distance Sensor lights on and off.
### Sound Blocks
Sound Blocks enable you to play sounds from your device or Hub.
#### Play Sound until Done
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt30c40fb8e68279a9/610bb03ca8995f47e0ee8aaa/gecko_block_help_flippersound_playsounduntildone_en.svg)

This block plays a selected sound on your device and pauses the programming stack until the sound is finished. Sounds can be added to the project using the Add Sound Button.
#### Start Sound
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt7b2b4d265d3c36e9/610bb002f84c0312b9895d4f/gecko_block_help_flippersound_playsound_en.svg)

This block starts playing a selected sound on your device and immediately plays the next block in the programming stack. Sounds can be added to the project using the Add Sound Button.
#### Play Beep for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt22e8dea3357fcdb4/610bafcaf40ded56bf47e0c2/gecko_block_help_flippersound_beepfortime_en.svg)

This block plays a beep tone on your Hub for a speciﬁed number of seconds.
#### Start Playing Beep
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt61042b20f25b7806/610baf97bf6f0c5156158a09/gecko_block_help_flippersound_beep_en.svg)

This block plays a beep tone on your Hub. It'll keep playing until something in the program stops it.
#### Stop All Sounds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt38d95dc77adb1091/610baf6852ffda16464c3c51/gecko_block_help_flippersound_stopsound_en.svg)

This block stops all sounds that are currently playing (i.e., beeps and sound ﬁles).
#### Change Pitch Effect By
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltdc59a00e56168246/610bae91547aba65281773bc/gecko_block_help_sound_changeeffectby_en.svg)

This block changes the pitch or pan left/right effect of the sounds that are being played on the device. <br><br> The pan effect determines which speaker is emitting the sound, with \"-100\" being only the left speaker, \"0\" being normal, and \"100\" being only the right speaker.
#### Set Pitch Effect By
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9201810ba386fbc6/610bae54c4c6d514ef140821/gecko_block_help_sound_seteffectto_en.svg)

This block changes the pitch or pan left/right effect of the sounds that are being played on the device. <br><br> The pan effect determines which speaker is emitting the sound, with \"-100\" being only the left speaker, \"0\" being normal, and \"100\" being only the right speaker.
#### Clear Sound Effects
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt836a520569beeb8d/610bae1af1700c1004af653d/gecko_block_help_sound_cleareffects_en.svg)

This block sets both the pitch and pan left/right sound effect back to normal.
#### Change Volume
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltebf3177e83b48907/610baf34dd97ab70235d6cf2/gecko_block_help_sound_changevolumeby_en.svg)

This block changes the volume of the sound currently being played by a specified increment from the volume at which it's currently playing. The default volume is 100%.
#### Set Volume
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2407b7bf4e352908/610baefcbf6f0c51561589f1/gecko_block_help_sound_setvolumeto_en.svg)

This block sets the volume of the sound. The default volume is 100%.
#### Volume
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9a8dd01409b7e2b0/610baec4b856e6496ff448fd/gecko_block_help_sound_volume_en.svg)

This block reports the current sound volume.
### Event Blocks
Event Blocks are comprised entirely of Hat Blocks, meaning that they're always the first block in a programming stack and other blocks can only be attached under them. Hat Blocks are necessary to start a programming stack and will be triggered when a specified event occurs.
#### When Program Starts
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt45c075c95cea6c9a/610b8eb45b8b6772858392fb/gecko_block_help_flipperevents_whenprogramstarts_en.svg)

This block plays all of the blocks attached to it, sequentially from top to bottom, when the program starts. 
#### When Color Is
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf71fa900e4233ed9/610b8e7a4cb8184d448f7295/gecko_block_help_flipperevents_whencolor_en.svg)

This block plays all of the blocks attached to it when the Color Sensor detects a speciﬁed color. The detectable colors are: <ul><li>(0) Black </li><li> (1) Violet </li><li> (3) Blue </li><li> (4) Light Blue </li><li> (6) Green </li><li> (7) Yellow </li><li> (9) Red </li><li> (10) White </li><li> (-1) no color</li></ul> This block will only trigger when it detects the speciﬁed color. This means that the block won't re-trigger if the detected color remains unchanged.
#### When Pressure Is
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt65f5c22b1346fd20/610babb86c90b352ad24494a/gecko_block_help_flipperevents_whenpressed_en.svg)

This block plays all of the blocks attached to it when the Force Sensor is pressed, hard-pressed, released, or when it detects any change in the pressure that's being applied. <br><br>This block will only trigger at the speciﬁed event. This means that the block won't re-trigger if the pressure on the Force Sensor remains unchanged.
#### When Closer Than
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte5199152f893f39e/610bab865b8b677285839805/gecko_block_help_flipperevents_whendistance_en.svg)

This block plays all of the blocks attached to it when the Distance Sensor detects that an object is closer than or further than the specified distance. <br><br>This block will only trigger at the speciﬁed event. This means that the block won't re-trigger if the distance remains unchanged.
#### When Tilted
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd3a74772b854fb1d/610bab52b856e6496ff44879/gecko_block_help_flipperevents_whentilted_en.svg)

This block plays all of the blocks attached to it when the Hub is tilted in the specified direction starting from a flat, button(s) up position.

The block will only trigger at the event of the Hub being tilted. That means that it won't trigger again as long as the Hub isn't tilted in a new direction.
#### When Hub Orientation Is Up
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb16500de4aa8307d/610bab20c1b18d71605d740a/gecko_block_help_flipperevents_whenorientation_en.svg)

This block plays all of the blocks attached to it when the Hub is placed in the specified orientation. The possible orientations are: <ul><li> (0) Top </li><li>(1) Front </li><li> (2) Right side </li><li> (3) Bottom </li><li> (4) Back </li><li> (5) Left side </li></ul>This block will only trigger at the speciﬁed event. This means that the block won't re-trigger if the orientation of the Hub remains unchanged.
#### When Hub Shaken
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt539201e662739440/610baaeee3dbbb493ef1f0a7/gecko_block_help_flipperevents_whengesture_en.svg)

This block plays all of the blocks attached to it when the Hub is: <ul><li> (1) Shaking</li><li> (2) Tapped </li><li> (3) Falling</li></ul>This block will only trigger at the start of the speciﬁed event. This means that the block won't re-trigger if the movement of the Hub remains unchanged.
#### When Hub Button Pressed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt1a211e7f8aed1cb3/610baab81e74574eb6e47bd1/gecko_block_help_flipperevents_whenbutton_en.svg)

This block plays all of the blocks attached to it when the Left or Right Buttons are pressed or released. <br><br>This block will only trigger at the speciﬁed event. This means that the block won't re-trigger as long as the state of the Buttons remains unchanged.
#### When Timer
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt64dc3b118618e694/637b4805f6a359125b37e041/gecko_block_help_flipperevents_whentimer_en.svg)

This block plays all of the blocks attached to it when the timer gets above a specified value.  The "timer" is a constantly running clock. It starts from "0" when the program starts. It can be reset using the <i>Reset Timer</i> Block.
#### When
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9413c572fcb7f1f5/61165a64833125163437b27a/gecko_block_help_flipperevents_whencondition_en.svg)

This block plays all of the blocks attached to it when a certain condition is true. <br><br>This block will only trigger at the event of the specified condition becoming true. This means that the block won't re-trigger if the condition remains true.
#### When I Receive Message
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt028a0812cddddc6b/610baa0e5f11974c0147216b/gecko_block_help_event_whenbroadcastreceived_en.svg)

This block plays all of the blocks attached to it when a speciﬁed message is broadcasted by the <i>Broadcast Message</i> Block or the <i>Broadcast Message and Wait</i> Block.
#### Broadcast Message
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltcac87a75a6a04620/61165a5b80ead51658dce5ee/gecko_block_help_event_broadcast_en.svg)

This block broadcasts a speciﬁed message. All of the <i>When I Receive Message</i> Hat Blocks that have been set to the specified message will play. After the message has been sent, the next block in the programming stack will play.
#### Broadcast Message and Wait
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3a0475e257e96de9/61165a4a3661bc1698fd63cb/gecko_block_help_event_broadcastandwait_en.svg)

This block broadcasts a speciﬁed message. All of the <i>When I Receive Message</i> Hat Blocks that have been set to the specified message will play. After the message has been sent, the block waits until all of the programming stacks with the specified message are ﬁnished before it proceeds to the next block in the stack.
### Control Blocks
The <i>Control Blocks</i> category contains all of the blocks that can modify the linear flow of block execution, such as “wait for” structures, loops, and conditions.
#### Wait for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt577a6b046ba2cf12/610ba95ee4c07e100f460a91/gecko_block_help_control_wait_vertical_en.svg)

This block pauses the programming stack for a speciﬁed number of seconds — it supports whole numbers and decimals.
#### Repeat loop
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltaf9eb8e984a28139/610ba91d6e185611518cdb47/gecko_block_help_control_repeat_vertical_en.svg)

All of the blocks held inside this block will loop a specified number of times before allowing the programming stack to continue.
#### Forever Loop
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt490703d8864c7d37/610ba8d50fd9536948f00eb2/gecko_block_help_control_forever_vertical_en.svg)

All of the blocks held inside this block will loop forever. <br><br>The only way to stop the loop is to interrupt the program by pressing the Stop Button, or by using the Stop All Block.
#### If Then
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt0657abb32d45dc79/610ba87b3a9e927142a111f3/gecko_block_help_control_if_en.svg)

This block will check whether the specified boolean condition is true. <br><br>If the condition is true, all of the blocks held inside it will play. If the condition is false, the blocks will be ignored.
#### If Then Else
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltbf374c3c49b8e7a4/610ba82abf6f0c51561588c3/gecko_block_help_control_if_else_en.svg)

This block will check whether the specified boolean condition is true. <br><br>If the condition is true, the blocks held inside the first space will play and the stack will continue. If the condition is false, the blocks inside the second space will play.
#### Wait Until
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt070fbd3b55923c20/61165a28844c89162405ad3c/gecko_block_help_control_wait_until_en.svg)

This block pauses the programming stack until the speciﬁed boolean condition is true.
#### Repeat Until Loop
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd3c17d7a20e2b985/610ba7c46ed0954c1fbe4578/gecko_block_help_control_repeat_until_en.svg)

All of the blocks held inside this block will loop until the speciﬁed boolean condition is true. When the specified condition becomes true, blocks beneath it will play.
#### Stop Other Stacks
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltaea99fdad7c71884/610ba79303e5207494ec1f32/gecko_block_help_flippercontrol_stopotherstacks_en.svg)

This block stops all programming stacks except its own.
#### Stop
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt5ad0715642ef4fac/610ba763a8995f47e0ee8904/gecko_block_help_flippercontrol_stop_en.svg)

This block stops all programming stacks that are currently running, stops only its own programming stack, or exits the program.
### Sensor Blocks
Sensor Blocks receive information from the sensors (e.g., Color Sensor, Distance Sensor, Force Sensor, Gyro Sensor).
#### Is color?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3d6de91799b0c5bc/610ba7331e74574eb6e47b47/gecko_block_help_flippersensors_iscolor_en.svg)

This block returns “true” when the Color Sensor detects the speciﬁed color. The detectable colors are: <ul><li>(0) Black </li><li> (1) Violet </li><li> (3) Blue </li><li> (4) Light Blue </li><li> (6) Green </li><li> (7) Yellow </li><li> (9) Red </li><li> (10) White </li><li>(-1) No color</li></ul>
#### Color
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltbbb6d37e606160d2/610ba6f90d1da8514f8c17ad/gecko_block_help_flippersensors_color_en.svg)

This block returns the current value of the color detected by the Color Sensor. The detectable colors are: <ul><li>(0) Black </li><li> (1) Violet </li><li> (3) Blue </li><li> (4) Light Blue </li><li> (6) Green </li><li> (7) Yellow </li><li> (9) Red </li><li> (10) White </li><li>(-1) No color</li></ul>
#### Is reﬂected light?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt7d1eb30354a7f06f/610ba6c86a299a454888ca03/gecko_block_help_flippersensors_isreflectivity_en.svg)

This block returns “true” when the light reﬂected back to the Color Sensor is greater than, equal to, or less than the specified percentage.
#### Reﬂected Light
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd7c281687560b39c/610ba690b52eb36e7d471f77/gecko_block_help_flippersensors_reflectivity_en.svg)

This block reports the current value of light that's being reﬂected back to the Color Sensor.
#### Is pressed?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte790107d2ab85c46/610ba6563f2fea6fcef3fa3b/gecko_block_help_flippersensors_ispressed_en.svg)

This block returns “true” when the Force Sensor is pressed (> 0 newton), hard-pressed (< 5 newton), or released (= 0 newton).
#### Pressure
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc28e2513872e786e/610ba6237dd1856a9e92029a/gecko_block_help_flippersensors_force_en.svg)

This block reports the current pressure being applied to the Force Sensor in newtons or as a percentage. The sensor can detect 2-10 newtons.
#### Is distance?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt41e9efc2223fd8e9/610ba52467a3dd6e7e9fd357/gecko_block_help_flippersensors_isdistance_en.svg)

This block returns “true” when the Distance Sensor detects that something is closer than, further than, or exactly at a distance speciﬁed in centimeters, inches, or as a percentage.
#### Distance
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9c742c5d1a5b0d1e/610ba4f232f0f711e6d1685c/gecko_block_help_flippersensors_distance_en.svg)

This block reports the current distance the Distance Sensor is detecting in centimeters, inches, or as a percentage. The sensor's range is 0-200 centimeters or 0-78.74 inches.
#### Is tilted?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6d96a605c1d91208/610ba4c056d38c4ffc805568/gecko_block_help_flippersensors_istilted_en.svg)

This block returns "true" when the Hub is tilted in the specified direction starting from a flat, button(s) up position.
#### Is Hub orientation?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt75d2433db89b9ccc/610ba48c98a6d911f1730332/gecko_block_help_flippersensors_isorientation_en.svg)

This block returns “true” when the Hub is placed in the specified orientation. The possible orientations are: <ul><li> (0) Top </li><li>(1) Front </li><li> (2) Right side </li><li> (3) Bottom </li><li> (4) Back </li><li> (5) Left side </li></ul>
#### Is Shaking?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt82a264bb7acab66e/610ba45b6ed0954c1fbe4506/gecko_block_help_flippersensors_ismotion_en.svg)

This block returns “true” when the Hub is Force Sensor is either: <ul><li> (0) tapped </li><li>(2) shaking</li><li> (3) falling </li></ul>
#### Hub Pitch Roll Yaw Angle
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltdd9074d0f03cd1e7/610ba42942ee276d28c77293/gecko_block_help_flippersensors_orientationaxis_en.svg)

This block reports the Hub's pitch, roll, or yaw angle. <i>Pitch</i>, <i>roll</i>, and <i>yaw</i> are terms commonly used to describe an airplane's movement through air but they can apply to any object rotating in all three dimensions. When looking at an airplane: <ul><li>The <i>pitch angle</i> refers to the airplane's nose going up or down. </li><li>The <i>roll angle</i> refers to the airplane's wings going up or down. </li><li>The <i>yaw angle</i> refers to the direction of the airplane compared to the ground. </li></ul>
#### Set Hub Yaw Angle to 0
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6c69c7c870734cd4/610ba3f81b8b1c163b39dea9/gecko_block_help_flippersensors_resetyaw_en.svg)

This block sets the yaw angle of the Hub to “0.” By default, the yaw angle will be “0” in the direction in which the Hub is facing when the program starts.
#### Is Hub Button pressed?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte546d974ceb198b5/610ba39703e5207494ec1e96/gecko_block_help_flippersensors_buttonispressed_en.svg)

This block returns “true” if the Left or Right Button is pressed or released.
#### Timer
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6f909cb1c9ea9273/610ba366f1700c1004af6347/gecko_block_help_flippersensors_timer_en.svg)

This block reports the time, in seconds, since the program started. The timer restarts every time the program restarts. Use the Reset Timer Block to manually restart the timer.
#### Reset Timer
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf0921397bf72474b/610ba336d9c9b0716677ef21/gecko_block_help_flippersensors_resettimer_en.svg)

This block resets the timer.
### Operator Blocks
Operator Blocks perform all of the mathematical operations that can be done using numerical values.
#### Pick Random Number
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4241317aa6a38ffe/610ba30652ffda16464c3a1d/gecko_block_help_operator_random_en.svg)

This block picks a random number within the specified range, including both endpoints. You can specify whole numbers or decimals as the minimum and maximum values. If one of the numbers is a decimal, it'll report a decimal.
#### Plus
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blta59d400a5df09c6d/610ba2d72e12ca67e8878194/gecko_block_help_operator_add_en.svg)

This block adds two values and returns the result.
#### Minus
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2d50d7d039534654/610ba2a8498f7447f4b05193/gecko_block_help_operator_subtract_en.svg)

This block subtracts the second value from the ﬁrst value and returns the result.
#### Multiply
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blta0411ec578a96c5d/610ba27a76f3370f3d3de90f/gecko_block_help_operator_multiply_en.svg)

This block multiplies two values and returns the result.
#### Divide
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3c3526b18c7c3815/610ba24b5b8b677285839697/gecko_block_help_operator_divide_en.svg)

This block divides the second value by the ﬁrst value and returns the result.
#### Less Than
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9f7d6e6ffbf1aee9/610ba21d77546f6d2ee48826/gecko_block_help_operator_lt_en.svg)

This block checks whether the ﬁrst value is less than the second value. If it's less, it'll return “true.” If not, it'll return “false.”
#### Equal
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt5106aaf1e459ad35/610ba1ed6c16d57544f38b64/gecko_block_help_operator_equals_en.svg)

This block checks whether the ﬁrst value is equal to the second value. If it's equal, it'll return “true.” If not, it'll return “false.”
#### Greater Than
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3380449fc97ca037/610ba1be57d8715003ed0b6b/gecko_block_help_operator_gt_en.svg)

This block checks whether the ﬁrst value is greater than the second value. If it's greater, it'll return “true.” If not, it'll return “false.”
#### And
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltaf9482162bf0433b/610ba18ff1cf4c0e857285ed/gecko_block_help_operator_and_en.svg)

This block joins two Boolean Blocks with an “AND” condition.
#### Or
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt654d50538ea605e0/610ba1613b72a64d5a5a63c9/gecko_block_help_operator_or_en.svg)

This block joins two Boolean Blocks with an “OR” condition.
#### Not
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt987c814f440f5e77/610b9d8eb77258728bf30b26/gecko_block_help_operator_not_en.svg)

This block inverts the boolean value of the condition inside it.
#### Is Between
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6a86c3d5f1de1dd3/610ba134a575147347249508/gecko_block_help_flipperoperator_isinbetween_en.svg)

This block checks whether the ﬁrst value specified falls between the second and third specified values, including both endpoints.
#### Join Strings
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt54507b80ac9a9911/610ba1050fd9536948f00d68/gecko_block_help_operator_join_en.svg)

This block joins two text values and returns the result (e.g., if “hello” and “world” were input into the block, it would return “helloworld”).
#### Letter of String
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2b858c831be2ac93/610ba0d79209284eaf71a1b5/gecko_block_help_operator_letter_of_en.svg)

This block returns the character that occupies the specified position of the given string. As an example, "letter 1 of LEGO" will return "L."
#### Length of String
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9e09ff76d3f2f2eb/610ba0a79c449d624c571af5/gecko_block_help_operator_length_en.svg)

This block returns the number of characters contained in the given string. For example, if the input is “LEGO,” the block returns “4.”
#### String Contains
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt011721d1ba26b06d/610ba0788e916f6ba04702db/gecko_block_help_operator_contains_en.svg)

This block returns “true” if the specified character is contained in the specified string.
#### Mod
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte3291c1e12d5bfd5/610ba0481eba654d59a186d7/gecko_block_help_operator_mod_en.svg)

This block returns the remainder when the ﬁrst value is divided by the second value (e.g., when <i>10</i> is the ﬁrst input and <i>3</i> is the second, the block will report <i>1</i>; <i>10</i> divided by <i>3</i> gives a remainder of <i>1</i>). Negative numbers behave a little differently because a remainder must always be positive (e.g., <i>-10</i> mod <i>3</i> equals <i>2</i>, not <i>-1</i> because you have to multiply <i>3</i> by <i>-4</i> to have any remainder at all).
#### Round
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt983e2b57219cff44/610ba019e4c07e100f4608f7/gecko_block_help_operator_round_en.svg)

This block rounds the given number to the nearest integer. It follows the standard rules of rounding (i.e., decimals of .5 or higher are rounded up, whereas decimals of less than .5 are rounded down).
#### Math Functions
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc9ea9fca7841a006/610b9fea9a599b4c0c53a289/gecko_block_help_operator_mathop_en.svg)

This block performs the speciﬁed math function on a given number and reports the result.
### Variable Blocks
The <i>Variable Blocks</i> category contains all of the blocks linked to variables, lists (arrays), and My Blocks.
#### Variable
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt7d26b2b450f30d82/610b8bd119eb9857f91ece11/gecko_block_help_variable_en.svg)

This block reports the value of a variable. Whenever a variable is created, a version of this block appears with the variable's given name on it.
#### Set Variable To
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf1fa904e62c84e0a/610b8bcd2755074c1842b616/gecko_block_help_set-variable-to_en.svg)

This block sets the speciﬁed variable to the given value. The variable can be either a string or a number.
#### Change Variable By
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt62a49a4db677fd4a/61164b2effd778164aa1f5e9/gecko_block_help_change-variable-by_en-us.svg)

This block changes the speciﬁed variable by a given value. The change is from the specified amount from the value currently stored in the variable. For example, if my variable contains the value <i>4</i>, using the Change Variable By 3 Block would make the value change to <i>7</i>. Also, if the variable is a text string (not a number), the value of the variable is set to the quantity the variable was to be changed by. For example, if “my variable” contains “LEGO,” using the block shown above will change the value to “1.”
#### List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9739802536dbae06/610b8bcacdf1126398c19064/gecko_block_help_list_en.svg)

This block reports, as a string, the items contained in a list. Whenever a list is created, a version of this block appears with the list's name on it.
#### Add Item to List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt81823d54eca5e1c3/610b8bc79a599b4c0c539e8b/gecko_block_help_add-item-to-list_en.svg)

This block adds the specified item to the end of the speciﬁed list.
#### Delete Item in List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt056cd0dac606532e/610b8b47c269714ff18cbd37/gecko_block_help_delete-item-in-list_en.svg)

This block deletes the item that's currently occupying the specified position in the specified list.
#### Delete All Items in List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3ff10f66262de78b/610b8bc598a6d911f172fe5e/gecko_block_help_delete-all-items-in-list_en.svg)

This block deletes all of the items in the speciﬁed list.
#### Insert Item at Index in List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb845f0b0e5a7576b/610b8bc15f11974c01471be5/gecko_block_help_insert-item-at-index-in-list_en.svg)

This block inserts a specified item at a specific position in the specified list.
#### Replace Item at Index in List with Another Item
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2d6f53e7c7affd62/610b8bbf2277974ab619c939/gecko_block_help_replace-item-at-index-in-list-with-another-item_en.svg)

This block replaces the item at the specified position with a specified value.
#### Value of Item at Index in List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltfbd7057ea26ff30d/610b8bbd9db365541cd2eb9f/gecko_block_help_value-of-item-at-index-in-list_en.svg)

This block returns the value that occupies the speciﬁed position in a speciﬁed list.
#### Index Value of Item in List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf29c2ad5ddd594ff/610b8bb92277974ab619c937/gecko_block_help_index-value-of-item-in-list_en.svg)

This block returns the number of the position in a list where an item ﬁrst appears. If the item isn't contained in the specified list, it reports “0.”
#### Length of List
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd59adaa5a19891f3/610b8bb726f24152a2580d9f/gecko_block_help_length-of-list_en.svg)

This block returns the number of items contained in the specified list.
#### List contains?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt59f06c6f95b04447/610b8bb557d8715003ed071b/gecko_block_help_list-contains_en.svg)

This block returns “true” if the list contains the specified value in any position. The specified value must be an exact match for the value contained in the list. If none of the values in the list are equal to the specified value, it returns “false.”
#### Deﬁne Block
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltacaf3bf7906ab80c/610b8bb19db365541cd2eb99/gecko_block_help_de_ne-block_en.svg)

This block allows you to create your own block. A <i>My Block</i> is the group of blocks that’s attached to the Define Block.
#### My Block
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4dc305e42937fd9d/610b8baf547aba6528176d24/gecko_block_help_my-block_en.svg)

This is your block! It'll play whatever you've attached to the Define Block.
### Weather Blocks
The available Weather Blocks are based on forecasts, not current values. Students can play around with forecasts up to 240 hours ahead of the current time. <br><br>Weather Blocks will only work when you’re online because they fetch real time data.
#### Set Forecast Location
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltef1bad073b652eb4/610b9fba38df221412d14160/gecko_block_help_weather_setlocation_en.svg)

This block sets the location for which weather forecast data will be retrieved.
#### Forecast Location
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt1a9143c2fd722e71/610b9f8a5f11974c01471f75/gecko_block_help_weather_location_en.svg)

This block reports the location currently set by the Set Forecast Location Block.
#### Forecast Temperature
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt99a1af01ee57fa52/610b9f5a6c16d57544f38af8/gecko_block_help_weather_temperature_en.svg)

This block reports the temperature at the set forecast location in either Celsius or Fahrenheit.
#### Forecast Wind Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd7c63eb16e8bbda5/610b9f29c269714ff18cc108/gecko_block_help_weather_windspeed_en.svg)

This block reports the wind speed at the set forecast location in meters per second or miles per hour.
#### Is forecast?
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt199006a28ee7699f/610b9ef81e74574eb6e479d5/gecko_block_help_weather_iscondition_en.svg)

This block returns “true” if there's a match for the specified weather condition at the set forecast location.
#### Forecast Precipitation
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt7cc764e130201bd9/610b9ec685421d14e47551ba/gecko_block_help_weather_precipitation_en.svg)

This block returns, in millimeters or inches, the amount of rain, snow, or other water condensation that's expected to fall at the set forecast location at a given time.
#### Forecast Air Pressure
This block returns the atmospheric pressure, in hectopascal (hPa), at the set forecast location.
#### Forecast Wind Direction
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4364572f388a9354/610b9e966b5415556835d272/gecko_block_help_weather_winddirection_en.svg)

This block reports the wind direction at the set forecast location. The direction is given as a string: <ul><li>"N" for north </li><li> "NE" for northeast </li><li> "E" for east </li><li> "SE" for southeast </li><li> "S" for south </li><li> "SW" for southwest </li><li> "W" for west </li><li> "NW" for northwest</li></ul>
#### Set Forecast to Now
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt900821674dce42c5/610b9e6565fc15500910dffe/gecko_block_help_weather_resettimeoffset_en.svg)

This block sets the forecast time of the weather data to now.
#### Change Forecast Time By
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt84dc0358ad4f92dd/610b9e35562a230be3f39048/gecko_block_help_weather_changetime_en.svg)

This block changes the forecast time by a specified number of hours from the current set value. The time is based on a 24-hour clock.
#### Set Forecast to Future Time
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc854d9c57b9f920a/610b9dfed877830e7e3ee052/gecko_block_help_weather_setforecast_en.svg)

This block sets the weather forecast from 1 to 9 days into the future at a speciﬁed hour based on a 24-hour clock.
#### Forecast Time Difference
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt05f926b0c418a190/610b9dc5c5ca4e54226870df/gecko_block_help_weather_timeoffset_en.svg)

This block reports the number of hours that the forecast has been shifted into the future from the current time. For example, if the current time is 10:00 and the forecast time has been changed to 16:00 today, this block will return a value of “6.”
### More Motor Blocks
These blocks extend functionality of the Motor Blocks to give you even more programming possibilities!
#### Go to Relative Motor Position at Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltdf9ba794edfd111b/610bb2263a9e927142a1138b/gecko_block_help_flippermoremotor_motorgotorelativeposition_en.svg)

This block runs one or more motors to a relative position at a specified speed. Unlike the absolute position that's used in the <i>Go to Position</i> Block, the relative position has no range limit and can be preset with the <i>Set Relative Motor Position to 0<i/> Block. 
#### Set Relative Motor Position to 0
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltcfea5275e04cefcd/610bb258d9c9b0716677f171/gecko_block_help_flippermoremotor_motorsetdegreecounted_en.svg)

This block sets the relative position of one or more motors to a specified value. Use a value of \"0\" to reset the relative position.
#### Relative Motor Position
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltbf816bd722fa4188/610bb28a0fd9536948f01092/gecko_block_help_flippermoremotor_position_en.svg)

This block returns the number of degrees that the specified motor has turned since the program started or was reset by the <i>Set Relative Motor Position to 0</i> Block.
#### Start Motor with Power
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6c54d9421a277f78/610b9ce0f4082a66a0a259da/gecko_block_help_flippermoremotor_motorstartpower_en.svg)

This block will run one or more motors at a specified percentage of power forever. When running a motor according to speed, the power of the motor is regulated in order to maintain the speciﬁed speed. 
#### Motor Power
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4fbe7605052c21b8/610b9c9e35ff7a140733c475/gecko_block_help_flippermoremotor_power_en.svg)

This block returns, as a percentage, the power level currently being used on the specified motor.
#### Stop and Coast Motors
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt929c1c81c41195a6/610b9c6448d88f1380077786/gecko_block_help_flippermoremotor_motorsetstopmethod_en.svg)

This block specifies how the motor will stop when using a Motor Block with a specified duration, or the Stop Motor Block. The motor can stop in three different ways: <ul><li><i>Brake</i>: the default method in which the motor uses power to brake when stopping and applies friction to the motor afterward </li><li><i>Hold position</i>: the motor uses power to brake and actively moves the motor back to the position in which it stopped, if it is forced away from it </li><li> <i>Coast</i>: the power to the motor is cut when stopping </li></ul>
#### Set Motor Acceleration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltbe9d4c1232b9f7f1/638f5da8c4e42d3c8f2d46fe/gecko_block_help_flippermoremotor_motorsetacceleration_en.svg)

This block sets the acceleration and deceleration of one or more motors. The acceleration can be set to fast, medium or slow. The default acceleration is medium. 

A customs acceleration can be set by inputting a variable with two numbers separated by a space. The first number sets the acceleration, the second number sets the deceleration. The range is 1-10000 with higher numbers giving a faster acceleration. The default values are:
- Fast =10000
- Medium = 2000 for the Small Motor, 4000 for the Medium and Larger Motor
- Slow = 1000

### More Movement Blocks
These blocks extend the functionality of the Movement Blocks to give your even more  programming possibilities for your Driving Base.
#### Start Moving at Speed
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd9bddb6a921f606e/610b9b3af1700c1004af61ef/gecko_block_help_flippermoremove_startdualspeed_en.svg)

This block starts moving a Driving Base forever at the speed that's been speciﬁed for each motor. The ﬁrst specified speed value sets the speed of the left motor, and the second specified value sets the speed of the right motor.
#### Set Movement Motors to Brake at Stop
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt09fcd565e7ba8f53/610b99da85421d14e47550ea/gecko_block_help_flippermoremove_movementsetstopmethod_en.svg)

This block specifies how motors will stop when using a Movement Block with a specified duration, or the Stop Moving Block. The motor can stop in three different ways: <ul><li><i>Brake</i>: the default method in which the motor uses power to brake when stopping and applies friction to the motor afterward </li><li><i>Hold position</i>: the motor uses power to brake and actively moves the motor back to the position in which it stopped, if it is forced away from it </li><li> <i>Coast</i>: the power to the motor is cut when stopping </li></ul>
#### Set Movement Acceleration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9012acbbd415762a/638f5dc112ffdf1423aaa05d/gecko_block_help_flippermoremove_movementsetacceleration_en.svg)

This block sets the acceleration and deceleration of a Driving Base. The acceleration can be set to fast, medium or slow. The default acceleration is medium. A customs acceleration can be set by inputting a variable with two numbers separated by a space. The first number sets the acceleration, the second number sets the deceleration. The range is 1-10000 with higher numbers giving a faster acceleration. 
The default values are:
Fast =10000
Medium = 1800
Slow = 1000
### More Sensors

#### Raw Color
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltce4d77d125143617/610b994fe04540748db7b486/gecko_block_help_flippermoresensors_rawcolor_en.svg)

This block returns the raw red, green, or blue color reading from the Color Sensor. The color value range is 0-255.
#### Hub Acceleration
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd1319c266e79e9c6/610b990d2755074c1842b8a2/gecko_block_help_flippermoresensors_acceleration_en.svg)

This block returns the Hub's acceleration on the X, Y, or Z axis.
#### Hub Angular Velocity
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt5688cce2707258ca/610b98de1b8b1c163b39dc77/gecko_block_help_flippermoresensors_angularvelocity_en.svg)

This block returns the Hub's angular velocity, also called "gyro rate," on the X, Y, or Z axis.
#### Hub Orientation
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blte254b2d69ddde1dd/610b98ae9209284eaf71a03d/gecko_block_help_flippermoresensors_orientation_en.svg)

This block reports the current orientation of the Hub. The Hub can detect the following  orientations: <ul><li> (0) Top </li><li>(1) Front </li><li> (2) Right side </li><li> (3) Bottom </li><li> (4) Back </li><li> (5) Left side </li></ul>
#### Gesture
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt48b077931c985392/610b987e03e5207494ec1cea/gecko_block_help_flippermoresensors_motion_en.svg)

This block reports the current gesture performed on the Hub. The Hub can detect the following gestures: <ul><li> (0) tapped </li><li>(2) shaking</li><li> (3) falling </li></ul>
#### Set Hub Sensor Orientation
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf3f7d7091ad9918c/610b984e2e12ca67e8877f9a/gecko_block_help_flippermoresensors_setorientation_en.svg)

This block sets the orientation of the 6-axis Gyro Sensor to <i>front</i>, <i>back</i>, <i>top</i>, <i>down</i>, <i>left side</i>, or <i>right side</i>. Setting the orientation of the 6-axis Gyro Sensor changes the axis of other blocks that are using the Gyro Sensor, such as the <i>Hub Pitch Roll Yaw Angle</i> Block.
### Music Blocks
These blocks can be used to create musical sounds. Combine them all to create your own symphony!
#### Play Drum
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf950395384d8a5d8/610b981ee4c07e100f460797/gecko_block_help_flippermusic_playdrumforbeats_en.svg)

This block plays the speciﬁed drum for the speciﬁed amount of time, measured in beats.
#### Rest
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt43e879c422ff6cca/610b97ec2e12ca67e8877f8c/gecko_block_help_flippermusic_restforbeats_en.svg)

This block “plays” a rest for the speciﬁed amount of time, measured in beats.
#### Play Note
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3bd6f048523ef1f6/610b97bc48d88f1380077692/gecko_block_help_flippermusic_playnoteforbeats_en.svg)

This block plays the specified note for the speciﬁed amount of time, measured in beats.
#### Set Instrument
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt25074082e447d0ba/610b978c498f7447f4b04fb3/gecko_block_help_flippermusic_setinstrument_en.svg)

This block sets the instrument used in the Play Note Block.
#### Set Tempo
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2a4bdd0c33a41f5b/610b975bf43325469c880fa1/gecko_block_help_flippermusic_settempo_en.svg)

This block sets the tempo of the beat. The tempo is represented as <i>beats per minute (bpm)</i>. <i>60 bpm</i> means that one beat will be played every second.
#### Change Tempo
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf5586e51150615c7/610b972cf4082a66a0a258aa/gecko_block_help_flippermusic_changetempo_en.svg)

This block changes the tempo of the beat that’s currently playing. The tempo is represented as <i>beats per minute (bpm)</i>. <i>60 bpm</i> means that one beat will be played every second.
#### Tempo
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt18bdf836a393bdc4/610b96fcf4082a66a0a2589c/gecko_block_help_flippermusic_gettempo_en.svg)

This block reports the tempo that's currently set.
### Log and Visualize Data Over Time

#### Plot Value on Line
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt832ff848ca2c2fc6/610b96ce9c449d624c57197a/gecko_block_help_linegraphmonitor_linegraphaddto_en.svg)

This block captures the entered value and plots it against the current time on the line belonging to the specified color.
#### Line Value
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt2431362a8c7d1e16/610b969e6e185611518cd811/gecko_block_help_linegraphmonitor_linegraphgetvalue_en.svg)

This block reports the minimum, maximum, average, or last value collected on the line belonging to the specified color.
#### Clear Line
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt691c933a8421e965/610b9666547aba6528176f63/gecko_block_help_linegraphmonitor_linegraphclearline_en.svg)

This block clears the data from the specified line.
#### Clear Line Graph
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt97ca1f2ea5afc7ef/610b962103e5207494ec1cb0/gecko_block_help_linegraphmonitor_linegraphclear_en.svg)

This block clears all of the data from the line graph.
#### Line Graph Timer
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt29de2a6d0cf13752/610b95dd57a8e173db642918/gecko_block_help_linegraphmonitor_linegraphtimer_en.svg)

This block reports the time, in seconds, since the program started or the Reset Line Graph Time Block was executed.
#### Reset Line Graph Timer
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt3e9d86dc23f9c0e5/610b959b57d8715003ed095f/gecko_block_help_linegraphmonitor_linegraphresettime_en.svg)

This block resets the time reported on the line graph to "0."
#### Show Line Graph Fullscreen
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltdb9a2bb9e81ad0f1/610b955c98a6d911f17300a0/gecko_block_help_linegraphmonitor_linegraphfullscreen_en.svg)

This block shows the line graph in fullscreen or in a floating window.
#### Hide Line Graph
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt6eb35cc059659deb/610b95203ae7ad4aabb3ed0a/gecko_block_help_linegraphmonitor_linegraphhide_en.svg)

This block hides the line graph window.
### Bar Graph

#### Change Bar Value by
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt66e22288424b4f6f/610b94e616b9e7493f5fb1ea/gecko_block_help_bargraphmonitor_bargraphchangevalue_en.svg)

This block changes the selected colored bar by a specified amount on the Bar Graph.
#### Set Bar Value to
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt9df0ceb19cb3ef5b/610b94b603a36e71498735d3/gecko_block_help_bargraphmonitor_bargraphsetvalue_en.svg)

This block sets the selected colored bar by a specified amount on the Bar Graph.
#### Bar Value
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltf7bc6bf05ead497d/610b9485ee51d0115c380e13/gecko_block_help_bargraphmonitor_bargraphgetvalue_en.svg)

This block reports the value of the selected colored bar from the Bar Graph.
#### Clear Bar Graph
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc83f328a70dd0eae/610b94553f2fea6fcef3f760/gecko_block_help_bargraphmonitor_bargraphcleardata_en.svg)

This block clears the Bar Graph by setting all bar values to 0.
#### Show Bar Graph Fullscreen
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltba39fa817c94a9d7/610b9422e3dbbb493ef1ed45/gecko_block_help_bargraphmonitor_bargraphshow_en.svg)

This block shows the Bar Graph either in fullscreen or in floating window.
#### Hide Bar Graph
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt4599e3dd5dee8feb/610b93dcb2e37e67f3001a8f/gecko_block_help_bargraphmonitor_bargraphhide_en.svg)

This Block hides the Line Graph window.
### Display

#### Write on Display for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt00311c99e6633931/610b93136c90b352ad244590/gecko_block_help_displaymonitor_displaywritefortime_en.svg)

This block shows a string of text in the Display window, and will halt the programming stack for the specified number of seconds.
#### Write on Display
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt0a3533e3c297129b/610b92b44ba97b701caf4bbc/gecko_block_help_displaymonitor_displaywrite_en.svg)

This block shows a string of text in the Display window.
#### Set Image on Display for Seconds
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltc6eebddc9b67286f/610b8b7465fc15500910dbf6/gecko_block_help_displaymonitor_displaysetimagefortime_en.svg)

This block shows an image in the Display window, and will halt the programming stack for the specified number seconds.
#### Set Image on Display
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt965171654300650d/610b8ba756d38c4ffc80506a/gecko_block_help_displaymonitor_displaysetimage_en.svg)

This block shows an image in the Display window.
#### Next Image
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltd42baf22611f6dad/610b91be9db365541cd2ece7/gecko_block_help_displaymonitor_displaynext_en.svg)

This block shows the next image in the project.
#### Show Display Fullscreen/Window
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt891eea01125f0505/610b918ee372544d4b0a07c5/gecko_block_help_displaymonitor_displaysetmonitorfullscreen_en.svg)

This block shows what's on the Display in fullscreen or in a floating window.
#### Hide Display
![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb57cac2a0c40a18c/610b90fde1f4f046a35bd713/gecko_block_help_displaymonitor_displayhide_en.svg)

This block hides the Display window.
## Block Types
The Scratch programming language is made up of different types of blocks, each represented by a different shape.
### Hat Blocks
Hat Blocks are used to start a program. They have a rounded top so that other blocks can only be attached under them.
### Stack Blocks
Stack Blocks perform the main commands in a program. They're the blocks that can make the motors move and the lights light up!
### C Blocks
C Blocks are C-shaped blocks. They're placed between the beginning and the end of the loop or check whether a condition is “true.” All of the C Blocks can be found in the <i>Control</i> category.
### Reporter Blocks
Reporter Blocks hold values, which can be a number or a string. Among other things, they can hold a sensor reading or store the value of a variable.
### Boolean Blocks
Boolean Blocks are conditions that can either be true or false. They're used together with C Blocks to form the logic of a program.
### Cap Blocks
Cap Blocks are used to end scripts. They're shaped with a notch at the top and a ﬂat bottom so that you can't place any blocks below them. There are two Cap Blocks, both of which can be found in the <i>Control</i> category.
### Programming Stack
A <i>programming stack</i> is a number of blocks that have been put together.
# Legal Documents

## Terms of Use
Introduction
------------

This license for the LEGO® Education SPIKE™ Software (hereinafter the "App") is granted by LEGO System A/S, Aastvej 1, DK-7190 Billund, Denmark, CVR no. 47 45 87 14. The LEGO Group and any and all entities that control, are controlled by or are affiliated or under common control with the LEGO Group or LEGO System A/S are collectively referred to here in as “we”, “us,” or “our”. We provide certain third-party software subject to separate license terms either presented at the time of installation or otherwise provided with the App (“Third-Party Software”). Such Third-Party Software is not included in the meaning of the term “App.” By downloading or using the App or by clicking a box that states that you accept or agree to these Terms and Conditions, you acknowledge that you have read and understand these Terms and Conditions and signify your agreement to be bound by the terms set out herein. If you do not agree to the Terms and Conditions, you may not use the App. The App is distributed by us via several outlet partners, including via the Apple App Store, Google Play Store, Microsoft Windows store, and the LEGOeducation.com website. If you have obtained the App from any other source, it may be defective or significantly revised from the original product. Use of any modified version is at your own risk and we do not assume any liability in that respect. For U.S.: LEGO Brand Retail Inc. doing business as LEGO Education North America, 501 Boylston Street Suite 4103, Boston, Massachusetts, 02116. E-mail: orders@LEGOeducation.us For the rest of the world: LEGO Systems A/S doing business as LEGO Education International, Aastvej 1, DK-7190 Billund, Denmark. E-mail: customer.service@LEGOeducation.comProcessing of Personal Information and Use of Cookies
-----------------------------------------------------

Our [Privacy Policy][1] and [Cookie Policy][2] are an integrated part of these Terms and Conditions. For information on the processing of personal information collected online from children, please refer to our Privacy Policy. In respect of LEGO Education SPIKE, the LEGO Group may collect aggregated data relating to the use of a product to help improve product performance and offerings. However, the LEGO Group will not under any circumstances collect any personal data relating to individual users (including any teacher or student) through LEGO Education SPIKE. (LEGO Education is a business division within the LEGO Group and is responsible for the product and solution lines offered under the “LEGO Education” brand.) Any third parties acting on behalf of the LEGO Group are bound by the same rules and principles as the LEGO Group.


  [1]: http://www.lego.com/legal/legal-notice/privacy-policy-full
  [2]: http://www.lego.com/legal/cookieinfoUse of Content
-------

No rights are granted to you other than a non-exclusive, limited license to use the App on the terms expressly set forth in these Terms and Conditions, including any right to any enhancement or update. All information, materials, functions, and other content ("Content") contained in the App are our copyrighted property or the copyrighted property of our licensors or licensees. All trademarks, service marks, trade names, and trade dresses are proprietary to us and/or our licensors or licensees. We may terminate your further access to the App, change the App, or delete content or features in any way, at any time and for any or no reason. You may only use the App (a) to carry out non-commercial projects that involve the LEGO Education SPIKE; or (b) to, for non-commercial purposes, create content through activities described in (a) above. You may NOT: (1) permit other individuals or entities to use the App, unless you ensure that the other individuals or entities (a) understand that their use of the App is subject to the terms and conditions of these Terms and Conditions, and (b) agree to and comply with these Terms and Conditions; (2) reverse engineer, decompile, disassemble, or otherwise reduce the App or Content to a human-perceivable form (except to the extent that this restriction is expressly prohibited by law); modify or translate the App or Content; or create derivative works based upon the App or Content; (3) copy the App or Content (except for back-up purposes); (4) sell, resell, rent, lease, assign, distribute, or otherwise transfer the App or Content, or any of the licensed rights with respect to the App or Content; (5) transmit the App or Content on the Internet; (6) use the back-up copy other than as a replacement for the primary copy; (7) use the App for any commercial purpose; (8) remove any proprietary notices or labels in or on the App or Content; (9) use the App for any purpose related to the manufacture, marketing, sale, or distribution of plastic building bricks; (10) use the App to gain access to unencrypted data in a manner that defeats the digital content protection provided in the App, or use the App in an attempt to, or in conjunction with any device, program or service designed to, circumvent technological measures employed to control access to, or the rights in, a content file or other work protected by the copyright laws of any jurisdiction; (11) take any action that results in any part of the App being subject to a license that requires, or purports to require, as a condition of use, modification or distribution, that (a) any code that is or could become subject to the license be disclosed or distributed in source code form, or (b) others have the right to modify or create derivative works of any code that is or could become subject to the license; or (12) directly or indirectly export, re-export, download, transmit, or transfer the App in violation of any provision within these Terms and Conditions. Any use or transfer of the App or Content in violation of the above will lead to immediate, automatic termination of your license.Title
-------

All title, ownership, rights, and intellectual property rights in and to the App and Content, including the text, building instructions, and images within the App, and all copies hereof, shall remain with us and/or our suppliers and licensors. All rights not expressly granted to you under these Terms and Conditions are reserved to us and/or our suppliers and licensors. The App and all Content is protected by national copyright laws and international copyright treaties. LEGO, the LEGO logo, the Minifigure and the LEGO Education SPIKE logo are trademarks and/or copyrights of the LEGO Group. ©2019-2023 The LEGO Group. All rights reserved. For notices and licenses relating to Third-Party Software, please see the following file Licenses.Accounts
--------

Some services on the App may permit or require you to create a LEGO ID account to participate or to secure additional benefits. Please see the Terms and Conditions for LEGO ID [here][1]. We may suspend or terminate your ability to use the App or portion hereof in case of failure to comply with said Terms and Conditions for LEGO ID or any special terms related to a particular service.


  [1]: https://identity.lego.com/en-US/termsApp Distributors/Stores
-----------------------

You acknowledge that these Terms and Conditions are concluded between you and us only, and not with app distributers / stores, e.g. Apple, Inc., Google, Amazon, Samsung etc. (“App Distributors”). We, and not the App Distributers, are solely responsible for the App and the services and Content available therein. The parties agree that the App Distributors have no obligation to provide maintenance or support services with respect to the App. To the maximum extent permitted by applicable law, the App Distributors will have no warranty obligation whatsoever with respect to the App. You agree that we, and not the App Distributors, are responsible for addressing any claims by you or any third party relating to the App or your possession and/or use of the App, including, but not limited to: (i) product liability claims; (ii) any claim that the App fails to conform to any applicable legal or regulatory requirement; and (iii) claims arising under consumer protection or similar legislation. You agree that we, and not the App Distributors, are responsible for the investigation, defense, settlement, and discharge of any third party intellectual property infringement claim related to the App or your possession and use of the App. You represent and warrant that (i) you are not located in a country that is subject to a U.S. Government embargo, or that has been designated by the U.S. Government as a "terrorist supporting" country; and (ii) you are not listed on any U.S. Government list of prohibited or restricted parties. You agree to comply with all applicable third party terms of agreement when using the App (e.g. you must not be in violation of your wireless data service terms of agreement when using the App). The parties agree that the App Distributors and their subsidiaries are third party beneficiaries to these Terms and Conditions. Upon your acceptance of the Terms and Conditions, the App Distributors will have the right (and will be deemed to have accepted the right) to enforce the Terms and Conditions against you as third party beneficiaries thereof. You agree that your use of the App is subject to the usage rules set forth in the App Distributor’s then-current terms of service for downloading apps through the App Distributor.Indemnification
-------

You are responsible for maintaining the confidentiality of your username(s), password(s), and your account(s), as well as all activities that occur under your account(s). To the extent possible under applicable law, you hereby agree to indemnify, defend, and hold us, our licensors, licensees, distributors, agents, representatives, and other authorized users, and each of the foregoing entities' respective resellers, distributors, service providers, and suppliers, and all of the foregoing entities' respective officers, directors, owners, employees, agents, representatives and assigns (collectively the "Indemnified Parties") harmless from and against any and all losses, damages, liabilities, and costs (including settlement costs and any legal or other fees and expenses for investigating or defending any actions or threatened actions) incurred by the Indemnified Parties in connection with any claim arising out of any breach by you of these Terms and Conditions or claims arising from your use of the App and/or your account(s). You shall use your best efforts to cooperate with us in the defense of any claim. We reserve the right, at our own expense, to employ separate counsel and assume the exclusive defense and control of any matter otherwise subject to indemnification by you.No Warranty
-------

THE APP AND ALL THIRD-PARTY SOFTWARE IS PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, NON-INFRINGEMENT, OR ANY OTHER APPLICABLE STATUTORY WARRANTIES (TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW). THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE APP, AND THIRD-PARTY SOFTWARE, IS WITH YOU. SHOULD THE APP AND/OR THIRD-PARTY SOFTWARE PROVE DEFECTIVE, YOU (AND NOT THE LEGO GROUP OR ANY AUTHORIZED DEALER) ASSUME THE ENTIRE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION. SOME STATES AND COUNTRIES DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES, SO THE ABOVE EXCLUSION MAY NOT APPLY TO YOU. THE LEGO GROUP DOES NOT WARRANT THAT THE FUNCTIONALITY PROVIDED BY THE APP, THIRD-PARTY SOFTWARE, OR ANY PROJECTS BASED ON THE APP WILL MEET YOUR REQUIREMENTS OR THAT THE OPERATION OF THE APP, THIRD-PARTY SOFTWARE, AND SAID PROJECTS WILL BE UNINTERRUPTED OR ERROR FREE.Limitation of Liability
----------------------

IN NO EVENT WILL THE LEGO GROUP OR ANY OF ITS SUPPLIERS OR LICENSORS BE LIABLE TO YOUR FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY LOST PROFITS, LOST SAVINGS OR OTHER INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF OR INABILITY TO USE THE APP OR ANY THIRD-PARTY SOFTWARE, EVEN IF THE LEGO GROUP, ANY OF ITS SUPPLIERS OR LICENSORS OR AN AUTHORIZED DEALER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES; OR FOR ANY CLAIM BY ANY OTHER PARTY. THE LEGO GROUP’S SUPPLIERS AND LICENSORS MAKE NO WARRANTIES AND SHALL HAVE NO LIABILITY IN CONNECTION WITH THIS AGREEMENT. SOME COUNTRIES OR STATES DO NOT ALLOW THE LIMITATION OR EXCLUSION OF LIABILITY FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES SO THE ABOVE LIMITATION OR EXCLUSION MAY NOT APPLY TO YOU.Jurisdictional and Venue Issues
-------

These Terms and Conditions are governed by the laws of the country in which you acquired the license to the App. You acknowledge that the App is, and Third-Party Software provided with the App may be, subject to control under the export control laws and regulations of the United States of America and other countries and applicable global export control laws and regulations. You agree that you will not directly or indirectly export, re-export, transfer, download, or ship the App or any Third-Party Software via any means: (a) to any prohibited destination, entity or individual without the required export license(s) or authorization(s) from the United States Government and/or other applicable export licensing authority, or (b) in violation of the laws and regulations of the United States of America or the laws and regulations of the jurisdiction in which you use or are downloading the App or any Third-Party Software provided with the App. If you are downloading the App, you represent and warrant that: (a) you are not located in, or under the control of, any country or state the laws and regulations of which prohibit importation of the App or any Third-Party Software provided with the App; and (b) you are not located in, or under the control of, any country or state to which the laws and regulations of the United States of America and/or other applicable export control laws prohibit exportation of the App or any Third-Party Software provided with the App. If you are an agency, department, or other entity of the United States Government: (a) you are notified that the App is a "commercial item" developed exclusively at private expense, consisting of "commercial computer software" and "commercial computer software documentation" as such terms are defined or used in the applicable United States acquisition regulations; and (b) the App is licensed hereunder (i) only as a commercial item and (ii) with only those rights as are granted to all other licensees pursuant to the terms and conditions of these Terms and Conditions. You agree not to use, duplicate, or disclose the App in any way not expressly permitted by these Terms and Conditions. Nothing in these Terms and Conditions requires the LEGO Group or any of our suppliers or licensors to produce or furnish technical data for or to you. We make no representation that Content in the App, or any content of the Third-Party Software, is appropriate or available for use in any particular location. Those who choose to access the App do so on their own initiative and are responsible for compliance with all applicable laws including any applicable local laws.Severance
-------

If any term or provision within these Terms and Conditions is or becomes invalid, illegal, or unenforceable for any reason, this shall not affect the validity or enforceability of the remainder of these Terms and Conditions. In such event, the term or provision deemed to be invalid, illegal, or unenforceable shall be deemed modified to the minimum extent necessary to make it valid, legal, and enforceable.Amendment
-------

At any time, we may amend these Terms and Conditions (including by modification, deletion, and/or addition of any portion hereof). If we make a material amendment to these Terms and Conditions, we will notify you of such amendment by posting notice thereof on the website LEGOeducation.com/support or via the relevant app store or the App itself. Any such amendment to these Terms and Conditions will be effective thirty (30) calendar days following publication of the aforementioned notice. By using the App following the thirty (30) calendar days' notice, you consent to any material amendments.Termination
-------

This license and your right to use the App shall terminate automatically if you fail to comply with the provisions of these Terms and Conditions. No notice shall be required from us to effectuate such termination. Upon termination, you are obligated to immediately destroy all copies of the App and Content. The following sections of these Terms and Conditions shall survive any termination of this license: “Title,” “No Warranty,” “Limitation of Remedies,” “Jurisdictional and Venue Issues,” and “Termination.
## Cookies
We use cookies or similar technologies on our digital applications.
-------------------------------------------------------------------

Cookies and similar technologies are small data files that your browser or app set on your computer or device. When sent to our servers, this information can help us deliver a more user-friendly and properly functioning service.

Our applications collect some information (e.g. information on IP addresses, browsers, operating systems, date stamps and time stamps). This information will not be linked to any other information we collect about you unless you have consented to it. But not every cookie is the same. For a list of the categories of cookies we use, see below. 

The cookies and similar technologies we use fall into two categories.

Required Cookies: These cookies and similar technologies are required to enable core app functionality and are therefore always enabled. This category includes your IP address, selected country and language and, in the event an error occurs, your usage of the app when such error occurs. When such information is collected, we will not ask for your consent, because we have a legitimate purpose – to ensure core functionality. Please note that you can opt-out of the other categories, but you cannot opt-out from sending required information. 

Tracking of Non-Personal Information: The tracking of this information is optional and allows us to track your usage of our app for statistical purposes to optimize your experience. We only use this information where the purpose is considered legitimate and does not require consent. The information that we collect is limited to anonymous and aggregated information which does not include any personally identifiable information. We will not ask to get your permission to collect this information, however you can at any time opt out by clicking on the settings tab and then selecting the opt out feature.
## Cookies
We use cookies or similar technologies on our digital applications.
-------------------------------------------------------------------

We use cookies or similar technologies on our digital applications.

Cookies and similar technologies are small data files that your browser or app sets on your computer or device. When sent to our servers, this information can help us deliver a properly functioning service – for example, reporting errors when they occur.

Our applications collect some information (e.g. information on IP addresses, browsers, operating systems, date stamps and time stamps). This information will not be linked to any other information we collect about you unless you have consented to it, and our use of such information will be limited to facilitating online communication or processes that are strictly necessary for functionality (collectively, “Strictly Necessary Cookies”).

Strictly Necessary Cookies: These are required to enable core app functionality and are therefore always enabled. This category includes your IP address, selected country and language and, in the event an error occurs, this information will be also sent to our servers to help us resolve the error. When such information is collected, we will not ask for your consent, because we have a legitimate purpose – to ensure core functionality.
## Privacy
Our Privacy Policy
------------------

Welcome to our privacy policy! It’s great that you’d like to know more about how we keep your information safe. This policy will give you information about how we look after your personal data when you visit our website (regardless of where you visit it from) or use our services or our applications (apps). The policy also tells you about your privacy rights and how the law protects you. So, if you’re looking for more information on how we collect, store, use and share your personal data we collect, this is the place for you! Now to start us off with, a couple of practical but highly important details for you to take note of!
## Accessibility
Accessibility
-------
LEGO Education is committed to ensuring effective communication and digital accessibility to as many users as possible. We are continually improving the user experience for everyone, and apply the relevant accessibility standards to achieve these goals. We welcome your feedback on the accessibility of spike.LEGOEducation.com. Please let us know if you encounter accessibility barriers in accessing any area our website.
## Certificates

### TECHNIC Large Hub, Y
Model: HUB NO.6
#### South Africa
TA-2019/1047![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)
### TECHNIC Large Hub, T
Model: HUB NO.6
#### South Africa
TA-2019/1047![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)
### TECHNIC Small Hub
Model: HUB NO.7
#### South Africa
TA-2021/1706![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt11320c393316e8bf/627cbada79aed9366938091b/ICASA_logo.png)