import json
import pickle
import pandas as pd

# right now, just for testing
# currently assigns a category arbitrarily

heroku = True

if not heroku:
	data_relative_path = "../../data/lincoln/"
else:
	data_relative_path = "./"

with open(data_relative_path + "donations_industry.json", 'r') as f:
    donations_industry = json.load(f)

df = pd.read_csv(data_relative_path + "current_social_media.csv", dtype=str)


# what it should do is load model from file when imported
# and score tweets using that
with open('bdt_model.sklearn','rb') as f:
	model = pickle.load(f)

def get_donors(user):
	print("user: ", str(user))
	ilist = donations_industry[df[df.twitter_id == user]["opensecrets"].values[0]]['response']['industries']['industry']
	return {i['@attributes']['industry_name']:i['@attributes']['total'] for i in ilist}

# print(get_donors("117501995"))

def get_subjects(text, threshold = -1, donors = None):
	if isinstance(text, str):
		text = [text]
	results = model.predict_proba(text)
	toreturn = []
	for i,r in enumerate(results):
		subjects = []
		zipped = list(zip(model.classes_,r))
		# print(zipped)
		sorted_zipped = sorted(zipped, key = lambda z: z[1], reverse = True)
		print(sorted_zipped)
		for z in sorted_zipped:
			# print (z[0])
			if z[1] >= threshold:
				if donors is None or z[0] in donors:
					subjects.append(z[0])
		toreturn.append(subjects)
	# print (toreturn)
	return toreturn

# def get_subjects(text, threshold, donors):
# 	return [donors]

def construct_message(user, relevant_industries, retweeted):
	message = df[df.twitter_id == user]["name"].values[0] + ", who "
	if retweeted:
		message += "retweeted"
	else:
		message += "tweeted"
	message +=  " below, received (in 2016 cycle):"

	# sorted_RIs = sorted(relevant_industries, key=lambda ri: ri[1], reverse = True)

	for ri in relevant_industries:
		next_line = "\n" + ri[0] + ": $" + ri[1]
		if len(message) + len(next_line) > 117:
			break
		else:
			message += next_line

	# if len(message) > 140:
	# 	message = message[:140]
	return message

def process(text, user, retweeted):
	donors = get_donors(user)
	# print(donors)
	subjects = get_subjects(text,.2,donors.keys())[0]
	# print(subjects)
	# no relevant industries --> no tweet
	if len(subjects) == 0:
		return False, ""

	relevant_industries = [(s,donors[s]) for s in subjects]
	return True, construct_message(user, relevant_industries, retweeted)

# print(process("It seems @realDonaldTrump still doesn't get it: @USCBO has debunked this claim. Stability of insurance markets will…", "171598736", True)[1])

def categorize(text):
	return (True, "VERY COOL TWEET")