#!/usr/bin/python3
# https://discordapp.com/oauth2/authorize?&client_id=517436515232645120&scope=bot&permissions=0
# 517436515232645120
import discord
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import random

cards = [
    "Base Game (US) 100 black cards, 500 white cards."
]
games = {

}

client = discord.Client()

def pick_username():
    return random.choice([
        "victory_royal",
        "obese_toaster",
        "kill_all_furries",
        "thot_patrol",
        "gamors_rize_up",
        "bonch_lasagna",
        "NEXT_MEME",
        "obama_bin_laden",
        "dedidaded_wam",
        "l33t_h4x0r",
        "ben_shapiro",
        "kanye2020_",
        "gamor_moment",
        "im_already_tracer"
    ])
def random_password():
    return random.choice([
        "h",
        "e",
        "waluigi",
        "dab",
        "fortnite",
        "epic",
        "yeet",
        "ill_be_tracer"
    ])

def read(f):
    with open(f, "r") as fi:
        return fi.read()

def new_game():
    driver = webdriver.Firefox()
    driver.get("https://pyx-3.pretendyoure.xyz/zy/game.jsp")
    print(driver.name)
    nickname = driver.find_element_by_id("nickname")
    submit_button = driver.find_element_by_id("nicknameconfirm")
    nickname.send_keys(pick_username() + str(time.time()).replace(".", "_"))
    submit_button.click()
    new_btn = driver.find_element_by_id("create_game")
    new_btn.click()
    for card in cards:
        driver.find_element_by_xpath("//label[@title='{}']".format(card)).click()

    pwd = driver.find_element_by_xpath("//input[@class='game_password']")
    password = random_password()
    pwd.send_keys(password)
    # click the menubar to apply
    driver.find_element_by_id("menubar").click()
    return (driver.current_url, driver, password)
    
def start_game(driver):
    print("trying to start")
    try:
        driver.find_element_by_id("start_game").click()
        print("started")
        driver.find_element_by_id("leave_game").click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        driver.quit()
        print("quit")
    except:
        print("nope")

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    print("Message Received")
    if message.content == "!newgame":
        print("Cards!")
        game_info = new_game()
        embed=discord.Embed(title="Cards Against Humanity",
                            url=game_info[0], 
                            description="Game Created! Join and add any reaction to start game")
        embed.add_field(name="password", value=game_info[2], inline=False)
        msg = await client.send_message(message.channel, embed=embed)
        await client.add_reaction(msg, "\U0001F44D")
        games[msg.timestamp] = game_info[1]

@client.event
async def on_reaction_add(reaction, user):
    if not user.id == client.user.id:
        print("Starting...")
        start_game(games[reaction.message.timestamp])

if __name__ == "__main__":
    client.run(read("token.dat"))
