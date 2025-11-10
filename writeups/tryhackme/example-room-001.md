# Example Room — TryHackMe Beginner (sample)
**Date:** 2025-11-10  
**Difficulty:** Beginner  
**Tools:** nmap, ssh

## Objective
Practice basic Linux enumeration and SSH.

## Recon
- `nmap -sC -sV -oN nmap_initial.txt 10.10.10.101` → open ports 22, 80

## Exploitation / Steps
1. Found web app on port 80 with login page.  
2. Enumerated default creds; found `admin:admin`.  
3. SSH with found credentials: `ssh admin@10.10.10.101`.  
4. Escalated to root using SUID binary `vulnerable_bin` (explain technique).

## Post-exploit / Lessons
- Basic nmap flags: `-sC -sV`.
- Look for SUID and cron jobs as privilege escalation paths.

## TL;DR
nmap → web → creds → ssh → SUID → root
