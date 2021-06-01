# Mirai

## What it does
The PeoplePerception class is a bit extensive. It uses two of NAOqi's APIs, ALPeoplePerception and ALTracker.
The class starts a background thread in which people from NAOqi's VisiblePeopleList and PeopleDetected data are compared.
When a person (who has a unique ID) is visible to the robot, it gets the data of that person (such as angle relative to the robot)
and puts it in an object. With every loop iteration the objects are updated or removed, depending on if that person is still
visible to the robot.

The objects are of the Person class, see its documentation for more info.

## Methods

### \_\_init\_\_(*mirai*)  
This method is called upon object creation and starts the processPeople method in a thread.

__Parameters__
- *mirai* - Instance of the Mirai class

### setDisappearTime(*time*)
Set the time to wait before considering someone to be not visible anymore for the NAOqi API.
 
__Parameters__
- *time* - Time to wait in seconds

### arrivedCallback(*person*)
Callback for when a person arrives which publishes an event on MQTT. Should not be changed.
 
__Parameters__
- *person* - Person who just arrived as instance of the Person class

### leftCallback(*person*)
Callback for when a person leaves which publishes an event on MQTT. Should not be changed.
 
__Parameters__
- *person* - Person who just left as instance of the Person class

### processPeople()
"Main" thread for this class. Makes sure the list of people is kept up to date, calls the callback functions and calls
other functions (such as coronaProofing) as well.

### findPerson(*id*)
Returns an instance of the Person class with the given ID. Returns False if no person was found.
 
__Parameters__
- *id* - ID of the person as string

### addPerson(*personToAdd*)
Adds an instance of the Person class to the list of people and calls arrivedCallback if the person is new.
Only used within the class.

__Parameters__
- *personToAdd* - Instance of the Person class to add

### coronaProofing()
Goes through the list of people and publishes an event on MQTT if people are too close to each other.

### getClosest()
Returns the instance of the person who is closest to the robot. Returns None if there are no visible people.

### trackClosest()
Uses the getClosest function to get the closest person, then calls the ALTracker API to track that person.

### trackPerson(*person*)
Tracks a person using the ALTracker API.

__Parameters__
- *person* - Instance of the Person class to track

### stopTracking()
Stops all tracking of the ALTracker API.

## Events

- Mirai/PeoplePerception/personArrived - called when a person arrives
- Mirai/PeoplePerception/personLeft - called when a person leaves
- Mirai/PeoplePerception/tooClose - called when people are too close to each other
