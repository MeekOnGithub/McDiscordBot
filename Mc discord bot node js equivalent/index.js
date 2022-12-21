const config = require('./config.json')
const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals } = require('mineflayer-pathfinder')
const { GoalNear } = goals

const discord = require('discord.js')
const client = new discord.Client({
    intents: 32767
});

const bot = mineflayer.createBot({
    host: config.minecraft.server.ip,
    port: config.minecraft.server.port,
    username: config.minecraft.username,
    password: config.minecraft.auth.password,
    version: config.minecraft.version,
    auth: config.minecraft.auth ? 'offline' : config.minecraft.auth.service
});

bot.loadPlugin(pathfinder)

client.on('ready', () => {
    console.log('le bot est prêt, faites ' + config.prefix + 'help pour avoir toutes les commandes');
});

client.on('messageCreate', (msg) => {
    if(msg.author.bot) return;
    if(!msg.content.startsWith(config.prefix)) return;
    if(msg.content.startsWith(config.prefix + 'help')) {
        const embed = new discord.EmbedBuilder({
            title: 'Commandes',
            description: 'Voici toutes les commandes du bot',
            color: 0x00ff00,
            fields: [
                {
                    name: 'help',
                    value: 'Affiche toutes les commandes du bot'
                },
                {
                    name: 'chat',
                    value: 'Envoie un message dans le chat du serveur'
                },
                {
                    name: 'goto',
                    value: 'Vas à des coordonnées (avec le pathfinder)'
                },
                {
                    name: 'stop',
                    value: 'Arrête le bot'
                }
            ],
            footer: {
                text: 'Bot développé par Entitymob#0667'
            }
        });
        msg.channel.send({ embeds: [embed] })
    } else if(msg.content.startsWith(config.prefix + 'chat')) {
        const args = msg.content.split(' ');
        args.shift();
        const message = args.join(' ');
        if(!args[0]) return msg.channel.send('Veuillez spécifier un message à envoyer dans le chat du serveur');
        bot.chat(message);
    } else if(msg.content.startsWith(config.prefix + 'goto')) {
        const args = msg.content.split(' ');
        args.shift();
        if(!args[2]) return msg.channel.send('Veuillez spécifier des coordonnées à atteindre (goto X Y Z)');
        const x = args[0];
        const y = args[1];
        const z = args[2];
        const goal = new GoalNear(x, y, z, 1);
        bot.pathfinder.setMovements(new Movements(bot, goal));
        bot.pathfinder.setGoal(goal);
    } else if(msg.content.startsWith(config.prefix + 'stop')) {
        bot.end();
        process.exit();
    }
});

client.login(config.token);