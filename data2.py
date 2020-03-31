import json

with open('jason_data.json') as f:
  data = json.load(f)

print type(data)

# get nodes

nodes = dict()
adj_list = []

author_id_to_node = {}
author_counter = 0

# loop through nodes
for i in data['nodes']:
  nodes[author_counter] = {'name' : i['author_name']}#, 'affl' : i['affil_name']}
  author_id_to_node[i['author_id']] = author_counter
  author_counter+=1

print "completed nodes"

# loop through links
for i in data['links']:
  adj_list.append([author_id_to_node[i['source']], author_id_to_node[i['target']], i['weight']])

print "completed links"

null = None
# final
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

print "----"
print res
print "---"
with open('data2.json','w') as json_file:
  json.dump(json.dumps(res), json_file)

# copy the above json file onto javascript
