# Emulation of Distance Vector Routing Protocol

In this project, we have implemented a CLI (Command Line Interface) program to emulate the D.V. routing protocol. Usage of the CLI is to engender real-time events in order to see how D.V protocol reacts to these events. D.V routing protocol, it is an asynchronous distributed routing protocol such that each node only needs its neighbors' distance vectors to perform routing.

### Inputs

Your only input is the Adjacency matrix which is all you need to create a network graph. Three examples of this matrix are shown below. we have read this through IO reading from a .txt file. multiple .txt file are available in the "**Python_Codes\TXTs**" directory.
 
### Emulation
The prominent part of this project is to mimic real scenarios that happen in the real world. The first important matter is the emulation time unit that is each iteration of our program. it is well-known that in the D.V routing protocol, after a node reaches a steady-state it halts the procedure of updating its distance vector waiting for one of these events:
1.	A change in connected links to itself
2.	Receiving an update of distance vector from one of its neighbors.

So, in summary, starting our program, follow this procedure for each node:  
1.	Initialize each distance vectors.  
2.	Put its distance vector into its neighbors’ queue (explained later) as it has sent its distance vector to its neighbors.  
3.	Update distance vector based on new information.  
4.	If its distance vector changed, we will return to state 2. Otherwise, we procede to state 5.  
5.	Wait for one of two supported events from CLI.  
6.	If the received event is not EXIT, go to state 3. Otherwise, end the program.  

### A note on nodes’ queue
In a real-world situation, each node is on a separate server and is connected to other nodes via the network. Still, in this project, we just want to emulate the D.V. protocol, and we don’t have any servers except a single process running this project. So to be able to simulate that asynchronous and distributed situation, we have a queue for each node. At each emulation time step, when our program starts to process a node, it checks its queue to see whether other nodes have been sent a distance vector for themselves or not (this queue acts like the network in the real-world situation). When a node wants to send other nodes a message, a distance vector in this case, it puts that message in other nodes’ queue.

### Events
In this project, we have two events:
1.	EXIT event, which indicates the end of the program.
2.	LINK UPDATE event. This event means a link’s metric has been changed. This event has to is received only by two endpoint nodes of links.

Also, The CLI enables users to see the distance vector of any nodes for all emulation time steps (that is the update steps of distance vector for each node).
