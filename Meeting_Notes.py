# Databricks notebook source
# Meeting of CTAS County Commission-Transcript of Dialogue

# COMMAND ----------

CTAS_meeting = """
Meeting of CTAS County Commission-Transcript of Dialogue

Chairman Wormsley (at the proper time and place, after taking the chair and striking the gavel on the table): This meeting of the CTAS County Commission will come to order. Clerk please call the role. (Ensure that a majority of the members are present.)

Chairman Wormsley: Each of you has received the agenda. I will entertain a motion that the agenda be approved.

Commissioner Brown: So moved.

Commissioner Hobbs: Seconded

Chairman Wormsley: It has been moved and seconded that the agenda be approved as received by the members. All those in favor signify by saying "Aye"?...Opposed by saying "No"?...The agenda is approved. You have received a copy of the minutes of the last meeting. Are there any corrections or additions to the meeting?

Commissioner McCroskey: Mister Chairman, my name has been omitted from the Special Committee on Indigent Care.

Chairman Wormsley: Thank you. If there are no objections, the minutes will be corrected to include the name of Commissioner McCroskey. Will the clerk please make this correction. Any further corrections? Seeing none, without objection the minutes will stand approved as read. (This is sort of a short cut way that is commonly used for approval of minutes and/or the agenda rather than requiring a motion and second.)

Chairman Wormsley: Commissioner Adkins, the first item on the agenda is yours.

Commissioner Adkins: Mister Chairman, I would like to make a motion to approve the resolution taking money from the Data Processing Reserve Account in the County Clerk's office and moving it to the equipment line to purchase a laptop computer.

Commissioner Carmical: I second the motion.

Chairman Wormsley: This resolution has a motion and second. Will the clerk please take the vote.

Chairman Wormsley: The resolution passes. We will now take up old business. At our last meeting, Commissioner McKee, your motion to sell property near the airport was deferred to this meeting. You are recognized.

Commissioner McKee: I move to withdraw that motion.

Chairman Wormsley: Commissioner McKee has moved to withdraw his motion to sell property near the airport. Seeing no objection, this motion is withdrawn. The next item on the agenda is Commissioner Rodgers'.

Commissioner Rodgers: I move adopton of the resolution previously provided to each of you to increase the state match local litigation tax in circuit, chancery, and criminal courts to the maximum amounts permissible. This resolution calls for the increases to go to the general fund.

Chairman Wormsley: Commissioner Duckett

Commissioner Duckett: The sheriff is opposed to this increase.

Chairman Wormsley: Commissioner, you are out of order because this motion has not been seconded as needed before the floor is open for discussion or debate. Discussion will begin after we have a second. Is there a second?

Commissioner Reinhart: For purposes of discussion, I second the motion.

Chairman Wormsley: Commissioner Rodgers is recognized.

Commissioner Rodgers: (Speaks about the data on collections, handing out all sorts of numerical figures regarding the litigation tax, and the county's need for additional revenue.)

Chairman Wormsley: Commissioner Duckett

Commissioner Duckett: I move an amendment to the motion to require 25 percent of the proceeds from the increase in the tax on criminal cases go to fund the sheriff's department.

Chairman Wormsley: Commissioner Malone

Commissioner Malone: I second the amendment.

Chairman Wormsley: A motion has been made and seconded to amend the motion to increase the state match local litigation taxes to the maximum amounts to require 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Any discussion? Will all those in favor please raise your hand? All those opposed please raise your hand. The amendment carries 17-2. We are now on the motion as amended. Any further discussion?

Commissioner Headrick: Does this require a two-thirds vote?

Chairman Wormsley: Will the county attorney answer that question?

County Attorney Fults: Since these are only courts of record, a majority vote will pass it. The two-thirds requirement is for the general sessions taxes.

Chairman Wormsley: Other questions or discussion? Commissioner Adams.

Commissioner Adams: Move for a roll call vote.

Commissioner Crenshaw: Second

Chairman Wormsley: The motion has been made and seconded that the state match local litigation taxes be increased to the maximum amounts allowed by law with 25 percent of the proceeds from the increase in the tax on criminal cases in courts of record going to fund the sheriff's department. Will all those in favor please vote as the clerk calls your name, those in favor vote "aye," those against vote "no." Nine votes for, nine votes against, one not voting. The increase fails. We are now on new business. Commissioner Adkins, the first item on the agenda is yours.

Commissioner Adkins: Each of you has previously received a copy of a resolution to increase the wheel tax by $10 to make up the state cut in education funding. I move adoption of this resolution.

Chairman Wormsley: Commissioner Thompson

Commissioner Thompson: I second.

Chairman Wormsley: It has been properly moved and seconded that a resolution increasing the wheel tax by $10 to make up the state cut in education funding be passed. Any discussion? (At this point numerous county commissioners speak for and against increasing the wheel tax and making up the education cuts. This is the first time this resolution is under consideration.) Commissioner Hayes is recognized.

Commissioner Hayes: I move previous question.

Commisioner Crenshaw: Second.

Chairman Wormsley: Previous question has been moved and seconded. As you know, a motion for previous question, if passed by a two-thirds vote, will cut off further debate and require us to vote yes or no on the resolution before us. You should vote for this motion if you wish to cut off further debate of the wheel tax increase at this point. Will all those in favor of previous question please raise your hand? Will all those against please raise your hand? The vote is 17-2. Previous question passes. We are now on the motion to increase the wheel tax by $10 to make up the state cut in education funding. Will all those in favor please raise your hand? Will all those against please raise your hand? The vote is 17-2. This increase passes on first passage. Is there any other new business? Since no member is seeking recognition, are there announcements? Commissioner Hailey.

Commissioner Hailey: There will be a meeting of the Budget Committee to look at solid waste funding recommendations on Tuesday, July 16 at noon here in this room.

Chairman Wormsley: Any other announcements? The next meeting of this body will be Monday, August 19 at 7 p.m., here in this room. Commissioner Carmical.

Commissioner Carmical: There will be a chili supper at County Elementary School on August 16 at 6:30 p.m. Everyone is invited.

Chairman Wormsley: Commissioner Austin.

Commissioner Austin: Move adjournment.

Commissioner Garland: Second.

Chairman Wormsley: Without objection, the meeting will stand adjourned.

"""

# COMMAND ----------

# AMI dialogues

# COMMAND ----------

ami_meeting = """
"C: Uh , making a profit of fifty million Euros . A: Alright so twenty five . D: Mm 'kay . C: So , it's go gonna have to be be pretty damn trendy . A: So yeah , I've The only the only remote controls I've used usually come with the television , and they're fairly basic . C: Yeah . D: Mm-hmm . C: Yeah . A: So uh Mm . C: Yeah , I was thinking that as well , I think the the only ones that I've seen that you buy are the sort of one for all type things where they're , yeah . D: Yeah the universal ones . D: Yeah . C: So presumably that might be an idea to put into . A: But but to sell it for twenty five you need a lot of neat features . B: Slim . A: For sure . D: Yeah . C: Yeah , yeah . C: Uh 'cause I mean , what uh twenty five Euros , that's about I dunno , fifteen Pounds or so ? D: Mm-hmm , it's about that . C: And that's quite a lot for a remote control . A: Yeah , yeah . D: Mm . D: Um well my first thoughts would be most remote controls are grey or black . D: As you said they come with the T_V_ so it's normally just your basic grey black remote control functions , so maybe we could think about colour ? C: Uh-huh . C: Mm-hmm . D: Make that might make it a bit different from the rest at least . D: Um , and as you say , we need to have some kind of gimmick , so um I thought maybe something like if you lose it and you can whistle , you know those things ? C: Okay . C: The the keyrings , yeah yeah . D: Because we always lose our remote control . A: Right . C: Okay , that's cool . B: Uh yeah uh , being as a Marketing Exper Expert I will like to say like before deciding the cost of this remote control or any other things we must see the market potential for this product like what is the competition in the market ? B: What are the available prices of the other remote controls in the prices ? B: What speciality other remote controls are having and how complicated it is to use these remote controls as compared to other remote controls available in the market . C: Okay . B: So before deciding or before finalising this project , we must discuss all these things , like and apart from this , it should be having a good look also , because people really li uh like to play with it when they are watching movies or playing with or playing with their C_D_ player , M_P_ three player like any electronic devices . D: Okay . D: Mm . D: Mm-hmm . D: Mm-hmm . B: They really want to have something good , having a good design in their hands , so , yes , all this . D: Yeah . C: Okay . C: 'Kay . A: Uh , what do we think a What do we think a good size would be for this ? C: So , we're looking for 'Kay . C: We're Sorry , carry on . A: 'Cause I I know as you add more buttons to the remote it sometimes gets so big and clunky and there's just like a hundred buttons on it , or you could have a really small slim one but then you could lose it easily . D: Yeah . C: Mm-hmm . C: Mm-hmm . D: Yeah . D: Then you lose it , yeah . C: Okay . D: Kind of um , maybe more like a P_D_A_ kind of , just hand held , like , 'cause Yeah . C: For for uh remember we're trying to make it for twelve Euros fifty . D: No , I wasn't , no sorry I wasn't thinking of the screen of like a P_D_A_ but Okay . C: Okay well right we'll have to um I'll we're k having another meeting in half an hour so um we should all look into a bit uh , oh actually , no , we'll allocate . C: So you do the looking around at other remote controls . B: Yeah . C: Um , if you could maybe come up with sort of shapes and suggested shades or whatever , and you could look into um basically how how it's made I_E_ like how you make it all in one , how what sort of materials are available to you whatever . C: And obviously , other instructions will come from the personal coach . A: Right . C: Which will probably just usurp what I said so Shapes and colours and um basically how to make it attractive . D: So you want me to look at shapes and everything you said ? D: Yep . D: Okay . C: Uh . D: Mm-hmm . C: And you look at competition and design . B: Yep . C: Cool . D: Okay . A: Okay . C: So we have uh Um . A: Wait for emails ? B: Uh . A: Hmm . C: Okay , groovy . C: And no doubt we'll get um Sorry . D: Oh no , . D: Sorry it's okay . C: We'll get um warnings for next meetings as well . D: Okay , cool . C: Okay . C: I shall I can't imagine these are worth much . C: Okay . B: Hmm . C: Fashion into electronic . C: Okay . "
"""
