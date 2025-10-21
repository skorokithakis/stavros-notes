# Various issues

## Tailscale keeps breaking my Docker DNS resolution

I run Tailscale on my PC and Docker keeps being unable to resolve DNS hostnames. I try to build a container that upgrades Debian and keep getting `Temporary failure resolving 'deb.debian.org'`, for example.

[This comment on GitHub](https://github.com/tailscale/tailscale/issues/12108#issuecomment-2106489435) had the solution:

```
# Run this on the host.
sudo tailscale set --stateful-filtering=false

* * *

<p style="font-size:80%; font-style: italic">
Last updated on October 20, 2025. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
