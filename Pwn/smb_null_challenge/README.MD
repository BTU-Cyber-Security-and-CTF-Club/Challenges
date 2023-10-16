# SMB Null Challenge

players can connect to a smb share without authentication and get the flag.

## how to run it

you can also just run the server, the client was just added for proof of concept in the compose yaml.

run in this dir:

`docker-compose up`

sample log from docker-compose:

```
[+] Running 2/0
 - Container smb_server  Created                                                                                                                                                                  0.0s 
 - Container smb_client  Recreated                                                                                                                                                                0.1s 
Attaching to smb_client, smb_server
smb_server  | Impacket v0.11.0 - Copyright 2023 Fortra
smb_server  |
smb_server  | [*] Config file parsed
smb_server  | [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
smb_server  | [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
smb_server  | [*] Config file parsed
smb_server  | [*] Config file parsed
smb_server  | [*] Config file parsed
smb_server  | [*] Incoming connection (192.168.2.3,35320)
smb_server  | [*] AUTHENTICATE_MESSAGE (WORKGROUP\root,SMB_CLIENT)
smb_server  | [*] User SMB_CLIENT\root authenticated successfully
smb_server  | [*] root::WORKGROUP:::aaaaaaaaaaaaaaaa
smb_server  | [*] Connecting Share(1:IPC$)
smb_server  | [*] NetrShareEnum Level: 1
smb_server  | [*] Disconnecting Share(1:IPC$)
smb_server  | [*] Closing down connection (192.168.2.3,35320)
smb_server  | [*] Remaining connections []
smb_client  |
smb_client  |   Sharename       Type      Comment
smb_client  |   ---------       ----      -------
smb_client  |   IPC$            Disk
smb_client  |   ONE_DOES_NOT_SIMPLY_WALK_INTO_MORDOR Disk      'you shall not pass'
smb_client  | SMB1 disabled -- no workgroup available
smb_client exited with code 0
```