# Decrypt Audible audiobooks

To decrypt Audible audiobooks:

1. Use [audible-cli](https://github.com/mkb79/audible-cli) to get your activation bytes (run `audible quickstart`.
2. Use [Libation](https://github.com/rmcrackan/Libation) to decrypt audiobooks.

Also, with ffmpeg:

```bash
ffmpeg -y -activation_bytes <bytes here> -i  'book.AAX' -codec copy 'book.m4b'
```

List of useful programs: https://github.com/rmcrackan/AudiobookHub

OpenAudible is paid and expensive now.

* * *

<p style="font-size:80%; font-style: italic">
Last updated on June 23, 2024. For any questions/feedback,
email me at <a href="mailto:hi@stavros.io">hi@stavros.io</a>.
</p>
