# Writing Developer-Friendly APIs

## 1. Lesson 5 Intro
- so far you've:
	1. learned the importance of APIs
	2. used providers' APIs
	3. created your own APIs
- now the art of making a good API
- think from perspective of devs using your API
- good practices
	1. naming practices
	2. pro tips on supporting devs
		- proper docs
		- communication streams

## 2. Developer Friendly Documentation
- should help support performant APIs
- should be easy to nav
- should have pleasing look
	- not newspaper classifieds
	- check out Twilio
- *"Hello World" documentation* has boilerplate code for using API quickly
	- this is like a "get started" section
- *FAQs* for devs to scan for common questions
	- address constraints
	- address common *corner cases*
- *playgrounds* and *sand boxes*
	- test out endpoints
	- execute sample requests
- try to make it "fun, interactive and developer friendly"

## 3. Using Proper URIs
- summary: good URI paths, good use of HTTP verbs and status codes, good errors
- understand URI vs URN vs URL as distinct but related terms: https://danielmiessler.com/study/url-uri/
- URI as path to an API resource
- URIs refer to resources, not actions on those resources
- use *plural* for each resource name
- use HTTP verbs responsibly
	- `HEAD` and `GET` *only* provide info since callable by web crawlers and search engines
- take advantage of HTTP status codes for successful and erroneous responses
- make errors "concise, clear and informative"

## 4. Versioning
- imagine `GET /puppies` returns a puppy's MM/DD/YYY birthdate
- later we want to include time of birth
	- so will change format to HH:MM:SS DD/MM/YYYY
- how to add this feature without messing up existing users?
- *versioning* for adding functionality without breaking existing implementations
- method #1: endpoints
	- appending e.g. `/v1/` vs `/v2/` to path: `GET /v1/puppies`
	- if app both renders webpages and serves API, append `api`:  `GET /api/v1/puppies`
- method #2: HTTP headers
	- "GitHub implements versioning this way"
	- so `curl ${github_api_url} -I` could return something like:
```
HTTP/1.1 200 OK
X-GitHub-Media-Type: github.v3; param-full; format-json
```

## 5. Communicating with Developers
- reaching out to devs, and them reaching out to you, as very valuable
- blogs and forums allow back-forth comm
	- also create community around the API
- publish content on social media
- make sure to have sample code available that uses the API in cool ways
- mistakes: devs expect explanations, not hiding
	- announcements when problems arise
	- clear documentation of bugs and fixes
- don't just support your code, support your *users*!

## 6. Learning from the Best
- read from Twitter, Facebook, GitHub, wolframalpha and other API dev docs to see what they do best
- what do they do right?
- how can you implement that in your own app?

## 7. Course Wrap Up
- API fundamentals are crucial for any full-stack web dev
- now join active community groups
- now take on ever more challenging web API projects
