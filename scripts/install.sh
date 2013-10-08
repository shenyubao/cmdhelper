#!/bin/bash
echo "To Install CmdHelper"
echo "Any Questions mailto ssybb1988@gmail.com"
echo -n "1.Input Your ID(e.g. yubao1):"
read -a input_name

if [[ ! -d ~/.cmdhelper ]]
then
    mkdir ~/.cmdhelper
fi

if [[ -f ~/.cmdhelper/account ]]
then
   rm ~/.cmdhelper/account
fi

echo $input_name > ~/.cmdhelper/account

echo -n "2.Copying "