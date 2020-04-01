import json

with open('jason_data.json') as f:
  data = json.load(f)

print type(data)

# get nodes

nodes = dict()
adj_list = []

author_id_to_node = {}
author_counter = 0

author_affiliation = {} # key : value = author counter : affil

# loop through nodes
for i in data['nodes']:
  nodes[author_counter] = {'name' : i['author_name'],'affiliation':i['affil_name'].encode('utf-8').strip(), 'num_papers':len(i['papers'])}
  author_id_to_node[i['author_id']] = author_counter
  author_affiliation[author_counter] = i['affil_name'].encode('utf-8').strip()
  author_counter+=1

# create institution codes
unique_affiliations = list(set(author_affiliation.values()))

institution_node_id = {} # key : value = uw : 0
for i in range(len(unique_affiliations)):
  institution_node_id[i] = {'name': unique_affiliations[i]}

inst_adj_list = [] # link institutions

print "completed nodes"

# given inst name returns the corresponding node id
def get_inst_id(x):
  for i,j in institution_node_id.items():
    if j['name'] == x:
      return i

# loop through links
for i in data['links']:
  source_id, target_id = author_id_to_node[i['source']], author_id_to_node[i['target']]
  print i['source'], i['target']
  print source_id, target_id
  adj_list.append([source_id, target_id, i['weight']])
  source_affl, target_affl = author_affiliation[source_id], author_affiliation[target_id]
  inst_adj_list.append([get_inst_id(source_affl), get_inst_id(target_affl)])

print "completed links"

# final structure
res = {
  "display": {
      "nodes":nodes
  },
  "networks":{
      "coauthorship":{
          "layers":[{
              "edgeList": adj_list,
              'metadata': 'null',
              'nodes':{}
          }]
      }
  },
  'title':'COVID 19'
}

res = json.dumps(res)

###
# Heterogeneous graph - inst and authorships
###



# printing area
print "----"
#print inst_adj_list
#print institution_node_id
#print res
print "---"
#with open('data2.json','w') as json_file:
#  json.dump(json.dumps(res), json_file)



# copy the above json file onto javascript
