# User Stories

## User 1: Carolyn, Student learning CS independently
This student will want to select topics to learn, look through their learning progress and receive an analysis report, and select specific problems for practice. THis student will need to do problems, and submit their problems to the app for grading. Carolyn is not expected to be super technically skilled and will have an interface that does not require code or terminal commands.
### User 1 Cases
- View available topics to learn
- View learning progress
- View problem bank (problems should be tied to topics)
- Submit problems
- View solution

## User 2: Nikolay, Student Learning CS in Class
Nikolay will want to do everything that the above user does, but additionally view feedback and grades from the teacher, as well as submit work directly to the teacher. Nikolay is similarly not expected to interact with the program using code or terminal commands.
### User 2 Cases
- View curriculum
- View learning progress
- View assignments
- Submit problems
- View solution
- View teacher feedback

## User 3: Yilin, Teacher Using This to Teach CS
Yilin will want to evaluate student progress, view their solutions/submitted work, provide feedback to students, and select topics/problems which will be used for their curriculum. The teacher is expected to have some more knowledge, and it might be helpful to give the teacher the ability to interact with the program at a lower level of abstraction to add/remove problems.
### User 3 Cases
- Create curriculum
  - Specify problems from problem bank to include in curriculum
- View problem bank
- View available topics to learn
- View curriculum
- View student learning progress
- Create assignments
- View assignments
- View student problems
- View solution
- Provide feedback

## Use Cases
### View Available Topics to Learn
#### _Name:_v_avail_topic
#### _What it does:_ When a user navigates to this page/tab on the app it will populate a list of available topics. Topics the user has already learned/mastered/marked as complete will be labelled as such to make it easy for the user to see what they have done and what they need to do.
#### _Inputs (with type information):_ List of topics (python list), Topics user has completed (python list, can make this another column of the list of topics - mark a topics as 1 if completed or 0 if not completed), whether or not a refresh button has been pressed (similar to the degree audit on myplan, type is whether or not a key is pressed, boolean)
#### _Outputs (with type information):_A list of topics which clearly indicates which have been compelted and which hasn't (python list in a UI), these topics can be selected to navigate user to practice problems/instruction on that topic.

### View Learning Progress
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### View Problem Bank
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### Submit Problems
#### _Name:_
#### _What it does:_
#### _Inputs (with type information):_
#### _Outputs (with type information)_

### View Solution
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### Create Curriculum
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### View Curriculum
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### Create Assugnments
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### View Assignments
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### Create Feedback for Students
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### View Feedback
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_

### View Student Learning Process
#### _Name:_
#### _What it does:_
#### _Inputs (with type information)_
#### _Outputs (with type information)_


