import re

class Blocks_World:
	
	def __init__(self, n):
		# Dict is for keeping track of which stack the block is currently in
		self.dictionary = {}
		self.table = []
		# Populates the table n times with an array and its respective block
		self.populate_table(n)

	def populate_table(self, n):
		for i in range(n):
			self.table.append([i])
			self.dictionary[i] = i

	def to_s(self):
		print(self.table)

	def move(self, move_block, target_block):
		self.grab_block(move_block)
		self.add_block(move_block, target_block)
		
	def grab_block(self, block):
		stack_idx = self.dictionary[block]
		self.clear_stack(stack_idx, block)
		self.table[stack_idx].pop()

	def add_block(self, move_block, target_block):
		stack_idx = self.dictionary[target_block]
		self.clear_stack(stack_idx, target_block)
		self.place_and_update_block(stack_idx, move_block)

	def command(self, str):
		# Parses input to find the from/to blocks
		numbers = re.findall('\d+', str)
		move_block = int(numbers[0])
		target_block = int(numbers[1])
		if move_block == target_block:
			return "Invalid Input"
		else:
			self.move(move_block, target_block)

	def clear_stack(self, stack_idx, target_block):
		stack = self.table[stack_idx]
		# Iterates through the stack, resetting blocks that are not the target
		for block in reversed(stack):
			if (block == target_block):
				return
			else:
				current_block = stack.pop()
				self.place_and_update_block(current_block, current_block)		

	def place_and_update_block(self, stack_idx, block):
		# Adds the block to a stack and updates its dict position
		self.table[stack_idx].append(block)
		self.dictionary[block] = stack_idx

	def run_challenge(self):
		print("The answer is:\n")
		self.command("MOVE 1 ONTO 2")
		self.command("MOVE 5 ONTO 1")
		self.command("MOVE 9 ONTO 5")
		self.command("MOVE 8 ONTO 9")
		self.command("MOVE 6 ONTO 1")
		self.command("MOVE 2 ONTO 4")
		self.to_s()
		

Blocks = Blocks_World(10)
Blocks.run_challenge()

# Answer = [[0], [1], [], [3], [4,2], [5], [6], [7], [8], [9]]