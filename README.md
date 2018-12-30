# social_network_simulator

Ideas:

Person objects with traits. Such as personality traits (introvert, energetic, depressive, workaholic), hobbies (different classes that might have differentiators on how social the activity is, or if it related to some other hobby), and profession and/or work place (which might have it's own set or differentiators and trait couplings).

Persons might also have trackers for current energy level, happiness and material wellbeing

Traits influence how the trackers are adjusted in different situations, and persons evaluate expected change before deciding if they attend. Total state value is probably determined ?linearly/squarely? with distance below comfort threshold (might skip threshold upwards and have some rule of diminishing returns)

Events with expected trait association that persons can decide to attend

Meetings that only happen if certain invited people attend

On events and meetings people meet other attending people randomly, biased by prior liking. And this influences personal trackers and liking of the other people in relation to how the other people affected tracker updates.

People might need to track who they know, or at least who they like

Attraction might be a separate random matching of hidden traits that people cannot evaluate beforehand, but influences liking massively, and could trigger separate needs like intimacy.


TODO:

versions of attendance assessment:
- based only on own dynamic levels
- based on own dynamic levels and personality traits
- + attending peoples friendship points
- Q-learning

set "score" for how well they do, initially: energy * happiness * (1 - loneliness)

timestep updates:
- update dynamic levels when staying home based on traits
- update levels when attending an event based on number of attendees
- update levels based on method described in events bellow

friendship tracking:
- let all persons have a ranked list of friends, acquaintances (and partners/lovers?) and enemies? or no categories to begin with and only friendship points
- limit slots on each? based on extroversion level and/or other personality trait
- people like other people more (gains friendship points), whenever they meet and this increases their score level. In proportion to score increase.
- a certain level of friendship points is required to stay at a certain friendship levels
- friendship points decay, and higher levels of friendship has higher upkeep
- maybe use long and short term points, where long term barely decays unless negative score change when meeting

events:
- add a timestep loop with generic events that can be attended
- when people attend events a matching algorithm determines who they spend time with, based on friendship points, traits and levels. Who they meet and how well they match are a big factor in level update for event, and determines update of friendship points
- add some traits to events that people can match
- add the possibility of events hosted by a person
- make the host able to make invite only events
- make the host make open events with a limited max attendees
- add level update that is influenced by friendship points
