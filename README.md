# TASK 2
We had a task to make navigation in the json file, and were told that we can use our creativity, so I decided to make three options for user to choose what he/she wants to do. When we start, program asks us to enter a path to the file. Then it reads the file and show us something like this:
```python

Enter a path to the file please: twitter2.json
- - - - - - - - - - - -- - - - - - - - - - - -
Here we have a dict with 6 keys
- - - - - - - - - - - -- - - - - - - - - - - -
1. users
2. next_cursor
3. next_cursor_str
4. previous_cursor
5. previous_cursor_str
6. total_count
- - - - - - - - - - - -- - - - - - - - - - - -
1  I want to see all dictionary
2  I want to write a key of element
3  I want to stop exploring the file
- - - - - - - - - - - -- - - - - - - - - - - -
Enter a number (1-3) of offer please: 
```
As we can see, user is able to see what type of object we have and what it consists. Then we have 3 options: to see all, to choose one element to explore or to stop exploring the file. If user enter wrong number, he/she will see a warning and request to try again.
### Here we have three functions
```diff
- read_file(file_name)
```
This function reads file and returns data in dict
```diff
- navigation_for_all(text)
```
This function consists all navigation. I did it with recursion.
```diff
-main()
```
The main function which contains all functions and input of file.

## Conclusion
___I did like this task, because we had a chance to show our imagination. It was really fascinating to choose what kind of options user will have and how you can react on wrong entering the data. Again I understood more better how json file looks like and how to work with them.___



# Task 3
We had to work with twitter API. As soon as we got it, we needed to read the data with keys and then process this data. We found 'screen_name' and 'location' of user, found lattitude and longtitude and made a map. Finally we should made a site which will conect our program with web and twitter.
### Here we have 8 functions
```diff
-get_info(user_name)
```
The function returns json data in dict by using our twitter API.
```diff
-read_file(text_json)
```
The function processes the data and makes a list with dicts where we can see screen name and location of user
``` diff
-find_location(all_info)
```
The function finds lattitude and longtitude by location
```diff
-make_map(copy_to_add_loc)
```
The function makes a map with location of users and their names on the markers
```diff
-all_func(user_name)
```
The function contains all previous functions(like main but it is not)
```diff
-display_the_main_page()
```
The function makes the main web page
```diff
-eenter()
```
The function gets user name where it should make a search, and calls main function, finally returns the map
## Conclusion
___This was really coll experience. I needed to work with API, twitter, web sites, flask, maps, it is a awersome list i suppose) It was hard for me to understand how to put it together but it was fun, and finally I got a lot of new information and skills___
