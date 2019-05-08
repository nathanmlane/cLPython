
attendees = ["Nate", "Gary", "John",]
attendees.append("Ashley")
attendees.extend(["Hambino", "Gob",])
optional_invites = ["Jim", "Dwight",]

potential_attendees = attendees + optional_invites

print("There are currently", len(attendees), "attendees.", "Potentially", len(potential_attendees), ".")
