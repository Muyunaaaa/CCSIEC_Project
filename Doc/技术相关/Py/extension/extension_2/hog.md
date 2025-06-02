### **项目简介**

这是 CS 61A 课程的第一个项目，目标是通过实现一个简单的骰子游戏“Hog”来练习 Python 编程技能。该项目分为多个阶段，每个阶段都会要求你实现不同的功能。

在这个项目中，你将通过编写代码来实现游戏规则，设计策略，进行实验并改进策略，最终创建一个有趣的小游戏。项目的主要任务是让你熟悉函数式编程、状态管理、随机性、测试等概念。

------

这个项目的目的是帮助你实现并模拟《猪游戏》（Hog），并设计不同的策略来玩游戏。通过这个项目，你将应用控制语句、高阶函数等编程技术，来编写一个能够模拟这个游戏规则的程序。具体的规则已经详细列出了，下面是对这些规则的一些总结和建议：

### 游戏规则概述：

1. **掷骰子**：玩家可以选择掷一定数量的骰子（最多10个），每次掷出的骰子点数会累加到本回合的得分。
2. **Pig Out**：如果掷出的任何一个骰子是1，则当前回合得分为1分。
3. **Free Bacon**：如果玩家选择不掷骰子，玩家的得分是对方分数对应的π数列的数字加上3。特殊情况下（对方分数为0），得分为6。
4. **Swine Align**：如果两名玩家的得分的最大公约数大于等于10，当前玩家可以再来一轮。
5. **Pig Pass**：如果当前玩家的得分比对方少，且两者的差小于3，则当前玩家会继续进行下一轮。

### 任务安排：

项目分为多个阶段，并且要求按时提交：

- **Phase 1**：实现游戏的一部分逻辑，并在9月8日之前提交。虽然这是一个早期的阶段，但非常重要，因为它是完成整个项目的基础。
- **Phase 2及之后**：在9月11日之前提交完整的项目，建议尽早完成。

### 项目代码结构：

- `hog.py`: 这是你需要修改并提交的主要文件。你将在其中实现游戏的逻辑。
- `dice.py`: 包含骰子的相关功能，你需要调用这些功能来模拟骰子的掷出。
- `hog_gui.py`: 提供图形用户界面（GUI），你可以在游戏完成后通过它来与游戏进行交互。
- `ucb.py`、`ok`、`tests`等：辅助文件，包含一些帮助函数和自动评分工具。

### 重要的编程概念：

1. **控制语句**：通过条件语句（如`if-else`）来控制游戏的流程。
2. **高阶函数**：你将使用高阶函数来实现不同的策略，例如通过函数传递策略参数来控制是否继续掷骰子。
3. **递归**：有些规则，如Swine Align和Pig Pass，可能需要用递归来处理。
4. **最大公约数（GCD）**：Swine Align规则涉及计算两个分数的GCD。

### 实现建议：

1. **函数分解**：根据规则将游戏逻辑分解为多个小函数，确保代码清晰且容易调试。
2. **策略设计**：你需要设计至少一个策略函数来决定每轮是否掷骰子。这涉及到根据当前和对方分数做决策。
3. **调试和测试**：利用`ok`自动评分工具频繁测试你的代码，确保每个阶段的功能正常。





### **阶段 1：游戏规则**

在阶段 1 中，你的任务是实现游戏的核心逻辑，包括规则和得分计算。该阶段的目标是让你熟悉游戏流程的基本实现。

#### **问题 1：实现`roll_dice`函数**

你需要实现 `roll_dice` 函数，它模拟玩家掷骰子的行为。如果玩家掷到 1，则回合得分为 1；如果掷到其他数字，则返回该点数。这个函数涉及随机性。

```python
def roll_dice(num_rolls, dice=six_sided):
    """掷骰子的函数。"""
    result = 0
    for _ in range(num_rolls):
        roll = dice()
        if roll == 1:
            return 1  # 如果掷到 1，立即返回 1
        result += roll
    return result
```

#### **问题 2：实现`free_bacon`函数**

`free_bacon` 是一个规则，玩家可以通过不掷骰子来获得“免费”得分。这一得分是通过查看对方的得分来计算的。你需要实现一个 `free_bacon` 函数，计算玩家通过这一规则获得的分数。

```py
def free_bacon(opponent_score):
    """根据对方的得分计算免费得分。"""
    return 10 - (opponent_score % 10)
```

#### **问题 3：实现`take_turn`函数**

`take_turn` 是一个函数，它处理每个回合的得分计算。在每一回合中，玩家可能选择掷骰子，也可能选择使用“免费得分”规则。根据规则，回合的得分会有所不同。你需要处理不同的情况，并计算该回合的得分。

```py
def take_turn(num_rolls, opponent_score, dice=six_sided):
    """玩家在自己回合时的得分计算。"""
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
```

#### **问题 4：实现`play`函数**

`play` 函数是游戏的核心，它管理整个游戏的回合和得分。你需要实现一个 `play` 函数，处理两个玩家的得分并根据规则进行回合。

```py
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided, goal=100):
    """模拟两名玩家交替掷骰子，直到一个玩家的得分超过目标分数。"""
    while score0 < goal and score1 < goal:
        score0 += take_turn(strategy0(score0, score1), score1, dice)
        if score0 >= goal:
            break
        score1 += take_turn(strategy1(score1, score0), score0, dice)
    return score0, score1
```

**问题 5 (3 分)**

实现 `play` 函数，模拟一次完整的 Hog 游戏。玩家轮流掷骰子，直到其中一位玩家达到目标分数。

为了决定每一轮掷骰子的数量，每个玩家都使用自己的策略（玩家 0 使用 `strategy0`，玩家 1 使用 `strategy1`）。策略是一个函数，给定玩家的当前分数和对手的分数，返回当前玩家在这一轮要掷的骰子数量。每轮只调用一次策略函数（否则可能会破坏图形界面）。不用担心现在就实现策略，你将在第 3 阶段实现策略。

游戏结束时，`play` 函数返回两位玩家的最终总得分，格式为玩家 0 的分数在前，玩家 1 的分数在后。

### 提示：

- 你应该调用你已经实现的函数。
- 用三个参数调用 `take_turn`。每轮只调用一次 `take_turn`。
- 调用 `extra_turn` 来决定当前玩家是否由于 **Swine Align** 或 **Pig Pass** 规则而进行额外的回合。
- 可以通过调用提供的 `other` 函数来获取对方玩家的编号（0 或 1）。
- 可以暂时忽略 `say` 参数，你将在项目的第二阶段使用它。

### 规则说明：

- 玩家可以连续进行多于两次回合。例如，如果他们第一轮结束时的得分是 10 对 20，他们由于 **Swine Align** 规则再次进行回合。如果他们得分为 8，当前比分变成 18 对 20，他们再次进行回合，触发 **Pig Pass** 规则。如果他们得分为 12，当前比分为 30 对 20，他们会连续进行第四次回合。
- 注意：数学上不可能同时触发 **Swine Align** 和 **Pig Pass**。

在编写任何代码之前，解锁测试以验证你对问题的理解。

```
bash


复制代码
python3 ok -q 05 -u
```

解锁完成后，开始实现你的解决方案。你可以使用以下命令检查代码的正确性：

```
bash


复制代码
python3 ok -q 05
```

完成后，你将能够玩一个图形化版本的游戏。我们提供了一个名为 `hog_gui.py` 的文件，你可以从终端运行：

```
bash


复制代码
python3 hog_gui.py
```

图形界面依赖于你的实现，因此如果你的代码有任何 bug，它们将在界面中体现出来。这意味着你可以使用图形界面作为调试工具；但是，最好先运行测试。

注意：图形界面现在已生效！要获得更新版本，请重新下载此网页中的压缩文件，并拖动新版本的 `hog_gui.py` 和 `gui_files/` 目录。

### 提交：

确保在检查点截止日期之前提交你的工作：

```
bash


复制代码
python3 ok --submit
```

确保你完成了第一阶段的所有问题：

```
bash


复制代码
python3 ok --score
```

### 翻译总结：

这个问题要求你实现 `play` 函数，模拟一个完整的游戏过程，其中两个玩家轮流掷骰子，直到某个玩家达到目标分数。你需要使用玩家的策略来确定每次掷骰子的数量，并且考虑特殊规则 **Swine Align** 和 **Pig Pass**。游戏结束后，返回两位玩家的最终得分。

### 实现思路：

1. 通过 `take_turn` 进行每个玩家的回合。
2. 使用 `extra_turn` 来判断玩家是否可以继续进行额外回合。
3. 利用 `other` 获取对方的编号。
4. 需要按规则逐步实现，确保每个回合的逻辑正确。 p

### **阶段 2：评论**

在第二阶段，你将实现评论功能，在每一回合后打印有关游戏的评论，例如：“22 分！这是玩家 1 迄今为止获得的最大分数。”

评论函数接收两个参数：玩家 0 和玩家 1 的当前得分。它可以根据当前的分数或其他环境信息打印评论。由于评论内容可能因每一回合的得分而不同，所以评论函数始终会返回另一个评论函数，在下一回合调用。评论函数的唯一副作用是打印。

#### **评论实例**

`say_scores` 函数是 `hog.py` 中的一个示例，它是一个简单的评论函数，用于宣布双方的得分。注意，`say_scores` 返回的是它自己，这意味着每回合都会调用相同的评论函数。

```py
def say_scores(score0, score1):
    """一个宣布双方得分的评论函数。"""
    print("玩家 0 现在有", score0, "分，玩家 1 现在有", score1, "分")
    return say_scores
```

`announce_lead_changes` 函数是一个更复杂的高阶函数，它返回一个评论函数，用于宣布领先者的变化。每回合都会调用一个不同的评论函数。

```py
def announce_lead_changes(last_leader=None):
    """返回一个评论函数，用于宣布领先者的变化。"""
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('玩家', leader, '以', abs(score0 - score1), '分领先')
        return announce_lead_changes(leader)
    return say
```

#### **问题 6：在每回合结束后添加评论**

- **目标**：修改 `play` 函数，使其在每回合结束后调用评论函数，并打印相关信息，如当前分数或领先者变化。
- **解决方案**：你需要将评论函数作为参数传递给 `play`，并在每回合结束时调用该评论函数。每个评论函数返回另一个评论函数，用于下一回合。

#### **问题 7：宣布最高得分**

- **目标**：实现 `announce_highest` 函数，该函数返回一个评论函数，用于宣布某个玩家每回合获得的最大得分。
- **要求**：你需要比较每回合得分与之前的得分，并记录每个玩家迄今为止获得的最高得分。当玩家获得新的最高得分时，打印相关信息。

------

### **阶段 3：策略**

在第三阶段，你将尝试通过优化策略来提高游戏胜率。你将实现一些实验来评估不同的策略，并改进游戏玩法。

#### **问题 8：实现 `make_averaged` 函数**

`make_averaged` 是一个高阶函数，它接受一个函数 `original_function` 作为参数，并返回一个新函数。这个新函数通过多次调用 `original_function` 来计算平均值。每次调用时，它会传递相同的参数。

```py
def make_averaged(original_function, trials_count=10000):
    """返回一个新函数，它通过多次调用 original_function 来计算平均值。"""
    def averaged_function(*args):
        total = 0
        for _ in range(trials_count):
            total += original_function(*args)
        return total / trials_count
    return averaged_function
```

#### **问题 9：实现 `max_scoring_num_rolls` 函数**

你需要设计一个实验来找出掷骰子的最佳次数，即能获得最大平均得分的掷骰子次数。你可以使用 `make_averaged` 和 `roll_dice` 函数来进行此实验。

```py
def max_scoring_num_rolls():
    """找到能够最大化得分的掷骰子次数。"""
    averaged_rolls = make_averaged(roll_dice)
    best_roll = 1
    max_avg_score = 0
    for rolls in range(1, 11):
        avg_score = averaged_rolls(rolls)
        if avg_score > max_avg_score:
            best_roll = rolls
            max_avg_score = avg_score
    return best_roll
```

#### **问题 10：实现 `bacon_strategy` 函数**

`bacon_strategy` 是一种策略，玩家会在免费得分规则能够给自己带来至少 `cutoff` 分数时选择不掷骰子，其他情况下才会掷骰子。

```py
def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=4):
    """如果可以通过免费得分获得足够的分数，则选择 0，否则掷骰子。"""
    if free_bacon(opponent_score) >= cutoff:
        return 0
    return num_rolls
```

#### **问题 11：实现 `extra_turn_strategy` 函数**

这种策略可以利用额外回合规则。当玩家的分数触发额外回合时，选择不掷骰子。其他情况下，则执行 `bacon_strategy`。

```py
def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=4):
    """如果触发了额外回合，则选择不掷骰子，否则执行 `bacon_strategy`。"""
    if is_extra_turn(score, opponent_score):
        return 0
    return bacon_strategy(score, opponent_score, cutoff, num_rolls)
```



------

####  **问题 12：实现最终策略（`final_strategy`）**

你需要实现一个策略，结合前面所有的策略，并尽可能优化以获得高胜率。你的最终策略应该能够应对不同的情况，并根据当前的游戏状态选择最合适的操作。你可以结合以下策略：

1. **`extra_turn_strategy`**：如果可以触发额外回合，选择不掷骰子。
2. **`bacon_strategy`**：在免费得分规则能带来至少 `cutoff` 分数时，选择不掷骰子。
3. **临界值判断**：在自己领先时，尽量减少风险，选择较少的掷骰子。
4. **尝试迫使对方触发额外回合**：利用规则设置，让对方做出对自己有利的举动。

例如，你可以检查是否能通过掷 0、1 或 2 个骰子获得胜利，避免过度冒险，或者通过选择合理的 `num_rolls` 和 `cutoff` 参数来尽量提高得分。

你可以通过以下方式验证策略的正确性：

```
python3 ok -q 12
```

如果你已经完成了所有任务，可以使用以下命令运行所有测试，并查看是否有任何未通过的测试：

```
python3 ok
```

完成后，你可以提交项目：

```
python3 ok --submit
```

如果你有合作伙伴，记得将他们添加到提交中：

- 访问 [okpy.org](https://okpy.org/) 并将合作伙伴加入到提交中。

检查你的分数，以确认所有问题是否完成：

```
python3 ok --score
```

你还可以通过图形用户界面与自己的策略进行对战：

```
python3 hog_gui.py
```

### **恭喜你完成了 CS 61A 第一个项目！**

如果你还没有休息，现在可以放松一下，享受一场有趣的 Hog 游戏，或者邀请朋友一起来玩。

### **项目总结**

完成此项目后，你将学到很多关于 Python 编程、函数式编程和策略设计的知识。你将学习如何将游戏规则转换为代码，如何使用高阶函数来实现复杂的行为，并且理解如何通过实验和策略优化提高游戏胜率。

通过这个项目，你不仅学到了 Python 编程的技能，还加深了对算法和策略的理解，为后续的课程和项目打下了坚实的基础。

![image-20241220024906264](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241220024906264.png)