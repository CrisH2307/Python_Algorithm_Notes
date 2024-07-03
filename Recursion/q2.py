# Family structure
'''
Sean is a member of Ninja club. He has a weird family structure. Every male member (M) gives birth 
to a male child first and then a female child, whereas every female (F) member gives birth to a 
female child first and then to a male child. Sean analyses this pattern and wants to know what 
will be the Kth child in his Nth generation. Can you help him?
A sample generation tree is shown, where ‘M’ denotes the male member and ‘F’ denotes the female member. 

Note: 
The generation tree starts with a male member i.e. Sean. 
Every member has exactly two children. 
The given N and K will always be valid. 

Sample Input 1:
2
2 2 
3 4  

Sample Output 1:
Female
Male

Sample Input 2:
3
5 1 
3 1
4 4  

Sample Output 2:
Male
Male
Male 


Explain:
+ The family structure starts with Sean, who is male.
+ Every male member (M) gives birth to a male child first and then a female child.
+ Every female member (F) gives birth to a female child first and then a male child.
Given N (generation number) and K (position of the child in that generation), 
we need to determine whether the Kth child in the Nth generation is male or female.

Base Case:
    If n=1, Sean is the only member in the first generation, and he is always male. So, we return "Male".

Recursive Case:
    For n>1, to determine the gender of the Kth child in the Nth generation:
        Calculate the parent's gender in the previous generation using kthChildNthGeneration(n - 1, (k + 1) // 2).
        Determine the child's gender based on the parent's gender and the position kk:
            If the parent is male:
                If k is odd, the child is male.
                If k is even, the child is female.
            If the parent is female:
                If k is odd, the child is female.
                If k is even, the child is male.
'''


def kthChildNthGeneration(n, k):
    if n == 1:
        return "Male"  # Base case: Sean is always male in the first generation
    
    # Recursive determination of parent's gender in previous generation
    parent_gender = kthChildNthGeneration(n - 1, (k + 1) // 2)
    
    # Determine child's gender based on parent's gender and position (odd or even)
    if parent_gender == "Male":
        return "Male" if k % 2 == 1 else "Female"
    else:
        return "Female" if k % 2 == 1 else "Male"