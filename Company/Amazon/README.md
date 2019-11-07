[TOC]
## Amazon
### Reorder Data In Log Files

前提：字符串数组，有两种字符串：
- 开头第一个词是标签，后面只含有单词用空格连接。
- 开头第一个词是标签，后面只含有数字用空格连接。

目的：
1. 所有数字按照原顺序放在最后。
2. 单词按照字母表顺序排列，只有在两个单词一样的时候才考虑标签。

思路：
1. 首先确定space complexity是O(n), 因为要建立保存数字和单词的list。
2. 然后遍历一下input数组，用split()把字符串转成数组，逐个判断第二个是不是数字，
是的话，就append到数字list里，不是的话就append到单词list里，注意放到单词list里的应该是
split之后的数组。其中判断是不是数字可以用isdigit()。
3. 随后，首先sort()一下单词数组，因为要考虑两个单词一样的情况。
4. 最后用list推导式来重新排列，用sorted()把key设置为匿名lambda函数，只包括排除标签之外的元素。
5. 最后返回alpha和digit连接之后数组。

复杂度：
- time complexity: O(nlogn)
- space complexity: O(n)
---

### Critical Connections in a Network
前提：一个无向图，vertex个数是n，input如下：
- n：vertex的个数
- list：无向图的所有edge。list的list。

目的：找出所有的critical connection。去掉这个connection，连通分量会增加。

思路：
1. 首先，建立6个：
- dfn: 每个vertex的时间戳，初始化为-1。
- low：每个vertex和它的子树不通过他parent能到达的最小点，初始化为-1。
- parent：每个vertex的父节点。
- graph：list的dictionary，使用了collections.defaultdic(list)，记录了每个节点和它连接的节点。存储图。
- self.time：记录时间戳。
- res：输出。
2. 然后写Tarjan函数：
- 给input节点的dfn和low赋值为self.time。
- self.time增加1.
- 遍历和u（input）连接的节点v。
- 如果子节点v的dfn为-1，也就是没有遍历过。给parent[v]赋值为u。然后递归执行Tarjan(v).
然后，更新low[u] = min(low[u],low[v])。然后判断如果low[v]比dfn[u]大的话，就代表着[u,v]为critical cennection。append到res里。
- 如果子节点被遍历过，但是parent[u] != v，再更新一下low[u] = min(low[u],dfn[v])。
3. 最后对n个未遍历过的节点逐个执行Tarjan，如果dfn[i] != -1，则跳过。
4. 最后返回res。
---

### Two Sum
前提：一个数字的list，一个target数字。

目的：返回一个list，包含两个index，使得这两个index对应的input的和等于target。

思路：
1. 循环嵌套的time complexity是O(n^2)，所以使用hash table，time complexity变为O(n)。
2. 创建一个dictionary。
3. 遍历list，每次给hashtable加入key为target - list[i]，而value为i。
4. 这样子在遍历的过程中，如果list[i]在hashtalbe中有值，则返回[hashtable的value, i]。

复杂度：
- space complexity: O(n)
- time complexity: O(n)
---

### Number of Islands
前提：2D数组，1代表陆地，0代表海水，只要是水平和垂直没有陆地相连，就是一个独立的岛屿。

目的：返回一个数字，代表2D地图的岛屿数量。

思路：
1. 遍历地图上所有的点，如果是1，岛屿个数就加一。
2. DFS来清洗一个岛屿，分别对四个方向递归的执行DFS，把1换成0.
3. DFS的终止条件是超出边界，或者当前的点不是陆地。所以每次判断完之后要把当前陆地换成海水，然后四个方向递归。
---

### Copy List with Random Pointer
前提：一个单向链表，每一个node会有一个随机指针，指向任意node或者None。

目的：返回一个deep copy的链表。

思路：
- 深度拷贝使用一个dictionary，key和value都是node，key对应原来的node，value对应新的node。
- 这题也使用了collections.defaultdict()，默认的不是一个type，而是lambda返回一个node。
- 注意1：记得dictionary[None] = None
- 注意2：记得新node的next和random要连接旧node的next和random对应的新node。
---

### Longest Palindromic Substring
前提：一个字符串。

目的：返回最长的回文。

思路：
1. 就是用中心扩散法，这个容易理解。
2. 首先写一个辅助函数，输入一个string，左指针，右指针。返回以指针为中心的回文。
3. 然后遍历一下输入的string，分别考虑偶数和奇数回文的情况，分别返回比较大小。
4. 奇数就是helper(string,i,i)。
5. 偶数就是helper(string,i,i+1)。
---

### K Closest Points to Origin
前提：输入一个(x,y)坐标的list和一个K值。

目的：返回K个距离(0, 0)最近的坐标list。

思路：
1. 最简单的就是用list推导式，配合上sorted()，里面的key用一个lambda函数。
2. 然后返回前K个元素的list。
---

### LRU Cache
前提：设计一个数据结构，满足一下：
- get: 获取key对应的正数值，如果没有，返回-1
- put: 将key和value存储到数据库中，但是，不能超过它的容量，如果超过容量，则最久没有使用的删除，添加新的。
- get和put都属于一种使用，会把相关的元素自动放在最近使用过的。

目的：实现这个数据结构，构造__init__，put和get函数。

思路：
1. 使用collections.OrderedDict。
2. 在get时，为了使操作触发最近使用，先pop，再put。如果不在，就返回-1
3. 在put时，首先判断是不是存在了，因为不涉及增加新的值，不用考虑容量的问题。
4. 然后如果put的是新的值，在判断有没有超过容量，如果超过了，用popitem(last=False)去除第一个元素，再加入新的。如果没超过，则直接加入，同时让仓库容量+1。

重点：
- collections.OrderedDict()
- pop(key) 删除并且返回key对应的value。
- popitem(last=False) 删除并且返回最早进入的值。
---

### Most Common Word
前提：输入一个字符串，同时给定一个banned字符串list。返回除了banned里之外，最长出现在input字符串里的单词。

思路：
1. 暴力搜索吧，首先用replace(old, new)去掉标点。
2. 然后遍历一下
- 用lower()全部小写
- 用split()转换成list之后
3. 创建一个dictionary，记录每个不在banned里单词出现的频率。同时记录最长的长度，和最长的单词，每次遍历出来的item都和最长的长度比较，如果长，更新最长的长度和最长的单词。
4. 返回出现次数最多的。

重点：
- 在定义dictionary的时候，注意使用defaultdict(lambda：0)，这样子后来就可以直接用+=来增加单词出现的数量了。
---

### Prison Cells After N Days
前提：一排牢房，如果前一天左右两个监狱都有人或者都没人，则第二天，这个监狱有人，如果左右两边一个有人一个没人，则第二天，这个监狱没人。

目的：给定一个初始状态，再给定一个天数，返回那天的状态。

难点：天数可以超级多，如果常规做法，写一个while循环，必然TLE。

思路：
1. 对于一般问题，我们写一个while函数，按照规律逐天的计算每天的状态。
2. 但是这么做不行，因为有时候天数太多，超时了。
3. 所以找规律，14天一个周期，问题解决。

重点：
1. 周期为14，但是当N为14时，不能直接N = 0，因为0天的时候是不对的，当N除以14mode为0时，
N应该为14。所以time_limit = 14 if not N % 14 else N % 14。
2. 我们做while循环的时候因为最左右两边的永远是0，所以可以在for外面直接给这两个赋值。
---

### Subtree of Another Tree
前提：给定两个树，判断s树是不是t树的子树。

思路：
1. 写一个辅助函数，用来traverse一遍树，然后返回一个遍历树的字符串。（先序遍历）
2. 然后分别对两个树执行这个函数，如果其中一个in另外一个，则说明他是子树。
3. 有一点需要注意，返回字符串前要加一个特殊符号，为了避免{12}和{2}这种情况。
---

### Trapping Rain Water
前提：雨水收集问题，一个list，每个item代表一个宽度为1的挡板，问这个list能接多少雨水。

思路：
1. 使用two-pointer方法来求解。
2. 首先定义左右最大值，全部初始化为0。然后定义左右指针。初始化雨水值为0。
3. 然后开始向中间移动指针，while循环为left<right。
4. 然后看左右指针的值，每次都处理数值小的那一侧指针。
5. 然后先更新这一侧的最大值，然后雨水的量为最大值和当前指针的差，然后指针移动。
6. 最后返回雨水值。

重点：
- 处理左右两侧相对小的值是因为木桶原理。
- 然后在用更新后的max和当前指针做差，就是雨水值。
---

### Merge Two Sorted Lists
前提：两个排好序的链表，把他们合并为一个新的排序链表。

思路：
1. 直接用recrusive做，首先判断其中是否有None，如果有，返回非空的那个。
2. 然后比较两个链表第一个值，返回小的那个。其中返回之前，把小的那个的next和大的那个recursive一下，连接到小的那个的next。
---

### Minimum Cost to Merge Stones
前提：一个list代表一横行的石堆，每个数字代表石堆的石头数量。同时给定一个K值。

目的：一次合并K个连读的石堆，问把这个横行的石堆合并为一堆，最小花费多少（花费是K个石堆包含石头的个数和）。如果不能合并，返回-1。

思路：
1. 这道题非常难，我们把过程分为两部分。
2. 在之前首先判断一下是否可以被k合并为1堆，如果(n - 1)%(K - 1)等于0，则可以。不然就返回-1。
3. 首先，先算出stone[i]和之前所有石头重量的和。定义一个数组prefix[n + 1]，其中n是stone数组的长度，prefix[i]就是stone[i - 1]包含它和之前所有的和。这个在后面有用。
4. 然后开始写dp的核心，一个recursive函数。输入参数只有两个值，一个是i，一个是j，分别是stone的起点和终点。返回的是最小代价。
5. 第一步，先判断j - i + 1是否大于K，如果不是，直接返回0。
6. 第二部，把i~j不断分成2份，recursive的计算每小份儿的返回值，然后不断的寻找最小的情况。循环的步长是k-1。
7. 第三步，判断一下i～j是否可以被K正好合并，也就是看看(j - i)%(k - 1)是否为0，如果可以直接合并，返回值需要加上i～j的总石头数，也就是prefix[j + 1] - prefix[i]。
8. 最后，直接返回dp(0, n - 1)就可以了。
---

### Serialize and Deserialize Binary Tree
前提：把一个树字符化，然后在解字符化。

思路：
1. 这道题思路就是recursive，无论是字符化还是解字符化，都只要处理当前的node.val，然后recursive的处理左右子树。有一点需要注意的是对None的处理。None和“#”对应是个不错的选择。
2. 巧妙利用python中function的返回值如果是多个值用逗号连接，则返回一个tuple。
3. 这里我们选择先序遍历树的方式。
---

### Binary Tree Zigzag Level Order Traversal
前提：给一个树，按照偶数排从左到右，奇数排从右到左，输出一个list的list。

思路：
1. 首先明确这个题用DFS来做，当是偶数排的时候，node.val用append添加到最后，如果是奇数排，用insert(0, node.val)添加到开头。
2. 因为要记录深度，所以这个函数不返回数组，而是把result和level通过参数传递进去，直接在函数中修改。
3. 但是记住每当level加1的时候，记得给result添加一个新的list进去，放置新level的元素。（具体操作就是判断深度是不是比result数组里的元素大，当深度为0，数组的长度应该为1。如果深度增加了，数组长度应该也增加。）
---

### Find Median from Data Stream
前提：设计一个数据结构，有两个基本操作，第一就是放进去一个整数，第二个就是返回当前数据库里的中间值。其中如果是奇数个，返回中间那个，如果是偶数个，返回中间两个的平均值。

思路：
1. 利用python的heapq最小堆的这个特性，建立两个堆，一个small，一个large。确保large的数量和small的数量相等或者比它大1。（相等时是偶数个，大于1时是奇数个）
2. heapq只能建立最小堆，那怎么弄出来一个small一个large呢？large就是正常建立一个heap，每次pop都是最小的值，但是我们要得到small里最大的值该怎么办？把small里所有数都取负，然后放进去，那么最小的pop值就是最大的相反数了。
3. 然后在add时，每次都往small里加，放入的是large的pushpop值，然后再平衡一下small和large的个数。
4. 在取中间值的时候，判断一下small和large的个数，然后返回相应的值。用large[0]来取最小值，- small[0]取最大值。
---

### Add Two Numbers
前提：两个链表，分别代表两个数，链表从低位到高位，也就是把这个数反过来存到链表里。

目的：设计一个算法，求出这两个链表代表数的值，然后返回一个链表。也是反过来存储的。

注意：两个数没有任何前置0，除非它本身就是0。

思路：
1. 这题因为输入和输出都是逆序的，也就是从低位开始，所以问题变得简单了，一次遍历就可以搞定。
2. 添加一个carry，初始为0，每次遍历的时候都加上两个链表的值，然后carry % 10为输出的node.val，carry自己更新为carry // 10。
3. 直到while条件l1, l2, carry都为None时，才停止。
4. 记得返回的是链表的head。
---

### Prime Palindrome
前提：给一个正整数，返回不小于它的最小质数回文。

思路：
1. 首先写一个判断是不是质数的方程，先判断是不是小于2或者被2整除，因为质数必须大于1，所以质数从2开始算起，任何这两种条件的情况，只要判断这个input是不是等于2就可以了。如果通过了，就开始常规的质数辨认了，从3开始到input**0.5+1，间隔2来查找，只要是有可以整除的，就不是质数。否则就是。
2. 然后开始判断是不是回文，有一点，如果回文的个数是偶数，则它一定被11整除，所以除了11，只考虑个数是奇数的回文。
3. 加入判断语句如果input大于等于8小于等于11，则返回11。
4. 然后判断是不是回文，因为一共最大是10**8，不可能是偶数，那么只能是10的7次方，然后我们取前5位，也就是10的5次方为最大值，初始值是10的input位数整除2。在循环判断里，首先组成回文的整数，然后判断是不是prime并且大于等于input，返回结果就行了。
---

### Word Ladder
前提：给定两个单词，和一个字典list，从list找出最短的使startword变为endword的路径，返回变换的次数。
- 变换只能一次变换一个字母。
- 如果没有符合的变换，返回0。包括endword不在list里和没有路径可以使startword到endword。

思路：
1. 首先写一个函数，用来算出一个set(front)和set(wordlist)可能衍生的子树。首先对front里面的每一个单词，单词里的每一位，用每一个字母(26个)代替，然后组成一个新的set，在求一下这个set和wordlist的交集。返回。返回的就是front里的每个单词有效的转换。
2. 然后开始bi-BFS，首先建立front和end两个set，里面放的是beginWord和endWord，然后把worList也转换成set。（因为速度快），然后判断一下endWord是否在wordList里，不在就直接返回0。
3. 开始常规的BFS，while判断front是否为空。
4. 如果front和end有交集（&），则返回depth。
5. 然后depth加一，从wordlist里减去front，再用1的方程更新front。
6. 判断一下front和end的长度，永远让长度短的成为front。（减少branching factor）
7. 如果不行，就返回0。
---

### Merge k Sorted Lists
前提：输入一个链表list，每个链表都是排序过的。要求输入一个把所有链表排序的node。

思路：
1. 这题用python2来做。
2. 首先用list推导式来建造一个tuple的list，第一个值是node.val，第二个是node。
3. 然后用heap.heapify来把这个list转换成一最小堆。
4. 然后dummy = pointer = ListNode(0)
5. 然后进行while循环。（因为每个元素都参与了循环，所以时间是n*k。
6. 每次用heap[0]去除val最小的一个，然后进行一些判断，如果取出的node.next是空的，则直接heappop这个最小堆。因为这个链表已经遍历完了。如果不是空，则用(node.next.val, node.next)替换。（因为每次进行heap操作时都是K个元素，所以时间是logK）
7. 最后给pointer新建一个ListNode(ndoe.val)，pointer = pointer.next
8. 最后返回dummy.next。
---







