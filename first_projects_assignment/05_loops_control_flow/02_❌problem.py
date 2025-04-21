MAX_VALUE = 100

def main():
    curr_term = 0
    next_term = 1
    # print Fibonacci nums from 0 to 100
    while curr_term <= MAX_VALUE:
        print(curr_term)
        #(new var = 0 + 1 = 1 )
        term_after_next = curr_term + next_term
        # (0 = 1 = 1)
        curr_term = next_term
        # (1 = 1)
        next_term = term_after_next
        
        #  


if __name__ == '__main__':
    main()