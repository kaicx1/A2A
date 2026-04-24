async def handle_task(request) -> str:
    text_parts = [p.text for p in request.message.parts if p.type =='text']
    combined = ' '.join(text_parts)
    if combined.split()[0] == '!summarise':
        return 'This document discusses key findings and recommendations across several topics.'
    # ECHO skill: return the input unchanged
    return combined