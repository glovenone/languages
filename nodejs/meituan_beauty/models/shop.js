'use strict';
let Sequelize = require('sequelize');
let sequelize = new Sequelize('test', 'root', 'xlxl2015', {
  host: 'localhost',
  port: '3306',
  dialect: 'mysql',
  define: {
    timestamps: false,
    freezeTableName: true // Model tableName will be the same as the model name
  },
  logging: false
});
module.exports = city=> {
  city = city || 'bj';
  return sequelize.define('shop_' + city, {
    id: {
      type: Sequelize.INTEGER,
      autoIncrement: true,
      primaryKey: true,
      unique: true
    },
    name: Sequelize.STRING(100),
    shopid: Sequelize.STRING(100),
    addr: Sequelize.STRING(500),
    area: Sequelize.STRING(500),
    phone: Sequelize.STRING(20),
    level: Sequelize.INTEGER(10),
    num1: Sequelize.INTEGER(20),
    num2: Sequelize.INTEGER(20)
  });
};