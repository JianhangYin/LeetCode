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
