# Lesson 1: What's and Why's of APIs

## 1. Course Intro
- a number of projects leading to Meet & Eat backend
- understanding of how social apps work
- tips for designing API endpoints

## 2. Prerequisites
- Python: functions, classes, dicts, properties, decorators, lambdas
- Flask and SQLAlchemy
- understanding of OAuth2 flows
	- complete the Authentication and Authorization course
	- or read through Google's OAuth 2 docs
- Vagrant environment
	- VirtualBox + the [vagrant setup](https://www.udacity.com/wiki/ud388/vagrant) from before
	- rec to fork the [fullstack vm repo](http://github.com/udacity/fullstack-nanodegree-vm)
- dev accounts for Google and Foursquare API 

## 3. What are APIs
- Application Programming Interface
	- any method to comm btwn two code entities
	- think of them as "connection points in code" for one app to talk to another
- if you copy code from browser and paste into word processor, an API in your comp did that
- if you listen to music on your comp, a music playing app used API to send music to speakers
- expose features without exposing all internal code
	- Apple and MS allow apps to interface but without revealing the actual code
	- even OSS like ubuntu make entry points that are used by other devs

## 4. Web APIs
- the above was about how APIs work inside the same machine
- this course is about APIs across machines
- Web APIs: invoke code on another machine via internet
- Mashups: use data from multiple APIs to create a new app
- Why do apps provide APIs?
	- promoting own business
	- sharing data
	- giving users more functionality
	- gaining traffic and popularity
	- for some companies it's big rev stream, e.g. Twilio

## 5. Web API Protocols
- all these machines use diff OS, specs, data structures
- they comm using a **protocols**, sets of rules
	- **OSI Layers** (Open Systems Interconnection Model)
	- characterizes the parts of how systems comm but doesn't get caught in specifics
	- so the focus is *interoperability* rather than 
	- partitioned into abstraction *layers*, originally 7 layers
		- each layer serves the one above it and is served by the one below it
		- multiple protocols can exist in each layer
		- they all must receive and hand off to adjacent layers
- Analogy: send message inside multiple envelopes
	- Application Layer sends original message
	- Presentation Layer wraps the message in an envelope
	- Session Layer adds its own envelope with info about preparing the message
	- Transport Layer adds its own envelope with info about breaking it into packets
	- Network Layer adds its own envelope with info about routing the message to final destination
	- Data Link Layer adds info about rebuilding the message once it arrives
	- Physical Layer is where the message finally reaches!
- at physical layer, it's transmitted as stream of bits over physical medium (wires or signals)
- at the other end, it's processed in reverse order
- devs mainly focus on application layer in OSI model
- OSs usually handle lower layer complexities
- BUT it's good to learn more about the [OSI model](https://en.wikipedia.org/wiki/OSI_model)

## 6. Digging into the Application Layer
- HTTP as most popular application level protocol
	- series of client-server requests and responses
	- also FTP, SSH, POP, ...
- original OSI model has application layer as highest level for communicating across internet
- other protocols and techs exist, so let's add two layers:
	1. the "Web Service" on top of the application
	2. the "Message Formatting" on top of the Web Service

## 7. The Web Service Layer
- sits on top the application layer
- determines format for sending and receiving API interactions
- Simple Object Access Protocol (SOAP) uses XML
	- sits on top of HTTP but can also work with SMTP
- Representational State Transfer (REST)
	- alternative to SOAP
	- set of guidelines
	- leverages HTTP to transmit data
	- you know this one, so say it with me: it's verbs... VERBS!
- (me: here it's good to understand RPC)

## 8. Content Formatting Layer
- once we communicate, how do we format info to send/receive?
- Message Formatting Layer as containing languages that address this
	- focus on the data structures containing the info we'll communicate
	- implementations already exist: XML, JSON
- so, thinking about SOAP and REST and XML and JSON, which choices work best for your app?

## 9. Choosing the Right Technologies
- side-by-side comparisons btwn SOAP vs REST:
	- SOAP by MS in 1998
	- SOAP must use XML for data structures
	- SOAP works with HTTP or other application layer protocols
	- REST by Roy Thomas Fielding in 2000
	- REST focuses on resources and uses HTTP methods
	- REST can use any type of message format
	- REST implies following architecture constraints
- popularity (ProgrammableWeb): since 2005, REST has dominated
	- Why? HTTP is familiar and REST is easier to implement.

## 10. XML vs JSON
- compare messaging layer options
	- XML in 1997
	- XML uses tags like HTML for rigid data structure
	- JSON in 2001
	- JSON derived from JS
	- JSON condenses with fewer character
- which is most friendly to the end-user?
	- programmableweb shows that XML started strong but JSON gains year over year
	- as easily the most popular for new APIs

## 11. Quiz: Developer Discussions

## 12. Quiz: Developer Discussions

## 13. Quiz: Developer Discussions

## 14. REST Constraints

## 15. Quiz: Why Stateless?

## 16. Lesson 1 Wrap Up
