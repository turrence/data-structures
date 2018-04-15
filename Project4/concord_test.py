from hash_lin_table import *
from hash_quad_table import *
import filecmp

# Create stop words hash table
stop_words = HashTableLinPr(251)            # start with table size of 251, grow as needed
stop_words.read_stop('stop_words.txt')      # read in stop words, load hash table

# Create concordance hash table
concord = HashTableLinPr(251)               # start with table size of 251, grow as needed
concord.read_file('input1.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("Linear1 File compare:", filecmp.cmp('test1.txt','concord1.txt')) # will be True if files match

# Create concordance hash table
concord = HashTableLinPr(251)               # start with table size of 251, grow as needed
concord.read_file('input2.txt', stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test2.txt')       # save (write) concordance to file
print("Linear2 File compare:", filecmp.cmp('test2.txt','concord2.txt')) # will be True if files match

# Create stop words hash table
stop_words = HashTableQuadPr(251)            # st#art with table size of 251, grow as needed
stop_words.read_stop('stop_words.txt')      # read in stop words, load hash table

# Create concordance hash table
concord = HashTableQuadPr(251)               # start with table size of 251, grow as needed
concord.read_file('input1.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("Quad1 File compare:", filecmp.cmp('test1.txt','concord1.txt')) # will be True if files match

# Create concordance hash table
concord = HashTableQuadPr(251)               # start with table size of 251, grow as needed
concord.read_file('input2.txt', stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test2.txt')       # save (write) concordance to file
print("Quad2 File compare:", filecmp.cmp('test2.txt','concord2.txt')) # will be True if files match

concordTrial = HashTableLinPr(251)
concordTrial.read_file('trial1.txt', stop_words)
concordTrial.save_concordance('trial_test1.txt')

concordTrial = HashTableQuadPr(251)
concordTrial.read_file('trial_quad1.txt', stop_words)
concordTrial.save_concordance('trial_quad_test1.txt')
print('trial File Compare:', filecmp.cmp('trial_test1.txt', 'trial_quad_test1.txt' ))
