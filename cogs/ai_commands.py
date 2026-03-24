import discord
from discord.ext import commands
from discord import app_commands
import os
from openai import OpenAI

class AICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    @app_commands.command(name="ask", description="Ask AI a question")
    @app_commands.describe(question="Your question for the AI")
    async def ask(self, interaction: discord.Interaction, question: str):
        """Chat with GPT-3.5"""
        await interaction.response.defer()
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question}
                ],
                max_tokens=500
            )
            answer = response.choices[0].message.content
            
            # Split long responses into multiple messages if needed
            if len(answer) > 2000:
                for i in range(0, len(answer), 2000):
                    await interaction.followup.send(answer[i:i+2000])
            else:
                await interaction.followup.send(answer)
        except Exception as e:
            await interaction.followup.send(f"❌ Error: {str(e)}")

    @app_commands.command(name="imagine", description="Generate creative text")
    @app_commands.describe(prompt="Creative prompt for the AI")
    async def imagine(self, interaction: discord.Interaction, prompt: str):
        """Generate creative content"""
        await interaction.response.defer()
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Create something creative based on this: {prompt}"}
                ],
                max_tokens=500
            )
            result = response.choices[0].message.content
            
            if len(result) > 2000:
                for i in range(0, len(result), 2000):
                    await interaction.followup.send(result[i:i+2000])
            else:
                await interaction.followup.send(result)
        except Exception as e:
            await interaction.followup.send(f"❌ Error: {str(e)}")

async def setup(bot):
    await bot.add_cog(AICommands(bot))
