meta:
	number of nodes
	
node_adjacency:
	adjacency matrix for the nodes
	
input_steps:
	contains a file for each timepoint t, starting at 0
	There are 2N lines
	first N contain, on each line:
		# of item_spec requests for node i
		# for each item_spec, 4 space seperated numbers:
			# item id
			# amount
			# time needed
			# priority
	second N contain, on each line:
		# of item_spec recieved for node i
		# for each item_spec, 2 space seperated numbers:
			# item id
			# amount